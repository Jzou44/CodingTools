/* ============================================================
   Coding.Tools — Main JavaScript
   Vanilla JS, no frameworks.
   ============================================================ */

(function () {
  "use strict";

  /* ----------------------------------------------------------
     Scroll Animation Observer
     ---------------------------------------------------------- */
  function initScrollObserver() {
    var sections = document.querySelectorAll(".category-section");
    var cards = document.querySelectorAll(".tool-card");

    if (!sections.length && !cards.length) return;

    var observerOptions = {
      threshold: 0.1,
      rootMargin: "0px 0px -50px 0px",
    };

    var sectionObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("visible");
          sectionObserver.unobserve(entry.target);
        }
      });
    }, observerOptions);

    sections.forEach(function (section) {
      sectionObserver.observe(section);
    });

    var cardObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          var card = entry.target;
          var parent = card.parentElement;
          var siblings = parent
            ? Array.from(parent.querySelectorAll(".tool-card"))
            : [];
          var index = siblings.indexOf(card);
          var delay = Math.min(index, 11) * 0.03;

          card.style.transitionDelay = delay + "s";
          card.classList.add("visible");
          cardObserver.unobserve(card);
        }
      });
    }, observerOptions);

    cards.forEach(function (card) {
      cardObserver.observe(card);
    });
  }

  /* ----------------------------------------------------------
     Search / Filter  (Homepage)
     ---------------------------------------------------------- */
  function initSearch() {
    var searchInput = document.getElementById("tool-search");
    if (!searchInput) return;

    var debounceTimer = null;

    searchInput.addEventListener("input", function () {
      clearTimeout(debounceTimer);
      debounceTimer = setTimeout(filterTools, 150);
    });

    function filterTools() {
      var query = searchInput.value.toLowerCase().trim();

      var cards = document.querySelectorAll(".tool-card");
      cards.forEach(function (card) {
        var text = card.textContent.toLowerCase();
        if (query === "" || text.indexOf(query) !== -1) {
          card.classList.remove("hidden");
        } else {
          card.classList.add("hidden");
        }
      });

      var sections = document.querySelectorAll(".category-section");
      sections.forEach(function (section) {
        var visibleCards = section.querySelectorAll(
          ".tool-card:not(.hidden)"
        );
        if (visibleCards.length === 0) {
          section.style.display = "none";
        } else {
          section.style.display = "";
        }
      });
    }
  }

  /* ----------------------------------------------------------
     Tool Page Interactions
     ---------------------------------------------------------- */
  function initToolPage() {
    var btnFormat = document.getElementById("btn-format");
    if (!btnFormat) return;

    var inputArea = document.getElementById("input-editor");
    var outputArea = document.getElementById("output-editor");
    var btnMinify = document.getElementById("btn-minify");
    var btnClear = document.getElementById("btn-clear");
    var btnCopy = document.getElementById("btn-copy");
    var btnDownload = document.getElementById("btn-download");
    var statusDot = document.getElementById("status-dot");
    var statusText = document.getElementById("status-text");
    var charCount = document.getElementById("char-count");
    var lineCount = document.getElementById("line-count");

    /* Format */
    btnFormat.addEventListener("click", function () {
      if (!inputArea || !outputArea) return;
      try {
        var parsed = JSON.parse(inputArea.value);
        outputArea.value = JSON.stringify(parsed, null, 2);
        setStatus("valid", "Valid JSON");
      } catch (err) {
        setStatus("invalid", err.message);
      }
      updateCounts();
    });

    /* Minify */
    if (btnMinify) {
      btnMinify.addEventListener("click", function () {
        if (!inputArea || !outputArea) return;
        try {
          var parsed = JSON.parse(inputArea.value);
          outputArea.value = JSON.stringify(parsed);
          setStatus("valid", "Minified");
        } catch (err) {
          setStatus("invalid", err.message);
        }
        updateCounts();
      });
    }

    /* Clear */
    if (btnClear) {
      btnClear.addEventListener("click", function () {
        if (inputArea) inputArea.value = "";
        if (outputArea) outputArea.value = "";
        setStatus("valid", "Ready");
        updateCounts();
      });
    }

    /* Copy */
    if (btnCopy) {
      btnCopy.addEventListener("click", function () {
        if (!outputArea || !outputArea.value) return;
        navigator.clipboard
          .writeText(outputArea.value)
          .then(function () {
            showToast("Copied!");
          })
          .catch(function () {
            /* Fallback for older browsers */
            outputArea.select();
            document.execCommand("copy");
            showToast("Copied!");
          });
      });
    }

    /* Download */
    if (btnDownload) {
      btnDownload.addEventListener("click", function () {
        if (!outputArea || !outputArea.value) return;
        var blob = new Blob([outputArea.value], { type: "text/plain" });
        var url = URL.createObjectURL(blob);
        var a = document.createElement("a");
        a.href = url;
        a.download = "output.txt";
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
      });
    }

    /* Status helper */
    function setStatus(type, message) {
      var statusMessage = document.getElementById("status-message");
      if (statusMessage) {
        statusMessage.className = "status-message " + type;
      }
      if (statusDot) {
        statusDot.style.display = (type === "valid" || type === "invalid") ? "inline-block" : "none";
        statusDot.className = "status-dot " + type;
      }
      if (statusText) {
        statusText.textContent = message;
      }
    }

    /* Count helper */
    function updateCounts() {
      if (!outputArea) return;
      var val = outputArea.value;
      var chars = val.length;
      var lines = val ? val.split("\n").length : 0;
      if (charCount) charCount.textContent = chars + " character" + (chars !== 1 ? "s" : "");
      if (lineCount) lineCount.textContent = lines + " line" + (lines !== 1 ? "s" : "");
    }

    /* Also update counts when output changes directly */
    if (outputArea) {
      outputArea.addEventListener("input", updateCounts);
    }
  }

  /* ----------------------------------------------------------
     Toast System
     ---------------------------------------------------------- */
  function showToast(message, duration) {
    if (typeof duration === "undefined") duration = 2000;

    var toast = document.createElement("div");
    toast.className = "toast";
    toast.textContent = message;
    document.body.appendChild(toast);

    /* Force reflow so the transition plays */
    toast.offsetHeight; // eslint-disable-line no-unused-expressions
    toast.classList.add("show");

    setTimeout(function () {
      toast.classList.remove("show");
      setTimeout(function () {
        if (toast.parentNode) toast.parentNode.removeChild(toast);
      }, 300);
    }, duration);
  }

  /* Make showToast globally accessible for inline handlers */
  window.showToast = showToast;

  /* ----------------------------------------------------------
     Smooth Scroll
     ---------------------------------------------------------- */
  function initSmoothScroll() {
    document.addEventListener("click", function (e) {
      var link = e.target.closest('a[href^="#"]');
      if (!link) return;

      var targetId = link.getAttribute("href");
      if (targetId === "#") return;

      var target = document.querySelector(targetId);
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: "smooth" });
      }
    });
  }

  /* ----------------------------------------------------------
     Init
     ---------------------------------------------------------- */
  document.addEventListener("DOMContentLoaded", function () {
    initScrollObserver();
    initSearch();
    initToolPage();
    initSmoothScroll();
  });
})();

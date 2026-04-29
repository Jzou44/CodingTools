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
     Init
     ---------------------------------------------------------- */
  document.addEventListener("DOMContentLoaded", function () {
    initScrollObserver();
    initSearch();
  });
})();

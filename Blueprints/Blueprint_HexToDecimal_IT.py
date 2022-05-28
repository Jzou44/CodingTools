from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_HexToDecimal_blueprint = Blueprint('Web_HexToDecimal_blueprint_IT', __name__)
template_dir = 'HexToDecimal/it/'

def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'it'
    return model

@Web_HexToDecimal_blueprint.route('/it/hex-to-decimal')
def hex_to_decimal():
    model = get_default_model()
    model['url'] = '/it/hex-to-decimal'
    model['enUrl'] = '/hex-to-decimal'
    model['headerTitle'] = 'Strumento di conversione online da esadecimale a decimale  - Coding.Tools'
    model['bodyTitle'] = 'Strumento di conversione online esadecimale o decimale'
    model['description'] = 'Questo strumento di conversione da esadecimale a decimale online ti aiuta a convertire un numero esadecimale in un numero decimale.'
    model['keywords'] = 'Da esadecimale a decimale, da esadecimale a decimale'
    model['image'] = '/image/cartoon-hex-to-decimal.png'
    return render_template(template_dir + 'template_hex_to_decimal_it.html', model=model)


@Web_HexToDecimal_blueprint.route('/it/decimal-to-hex')
def decimal_to_hex():
    model = get_default_model()
    model['url'] = '/it/decimal-to-hex'
    model['enUrl'] = '/decimal-to-hex'
    model['headerTitle'] = 'Strumento di conversione online da decimale a esadecimale  - Coding.Tools'
    model['bodyTitle'] = 'Strumento di conversione online decimale o esadecimale'
    model['description'] = 'Questo strumento decimale per conversione esadecimale online ti aiuta a convertire un numero decimale in un numero esadecimale.'
    model['keywords'] = 'Da decimale a esadecimale, da decimale a esadecimale'
    model['image'] = '/image/cartoon-decimal-to-hex.png'
    return render_template(template_dir + 'template_decimal_to_hex_it.html', model=model)


@Web_HexToDecimal_blueprint.route('/it/octal-to-decimal')
def octal_to_decimal():
    model = get_default_model()
    model['url'] = '/it/octal-to-decimal'
    model['enUrl'] = '/octal-to-decimal'
    model['headerTitle'] = 'Strumento di conversione online da ottale a decimale  - Coding.Tools'
    model['bodyTitle'] = 'Strumento di conversione online da ottale a decimale'
    model['description'] = 'Questo strumento di conversione da ottale a decimale online ti aiuta a convertire un numero ottale in un numero decimale.'
    model['keywords'] = 'Da ottale a decimale, da ottale a decimale'
    model['image'] = '/image/octal_to_decimal.png'
    return render_template(template_dir + 'template_octal_to_decimal_it.html', model=model)


@Web_HexToDecimal_blueprint.route('/it/decimal-to-octal')
def decimal_to_octal():
    model = get_default_model()
    model['url'] = '/it/decimal-to-octal'
    model['enUrl'] = '/decimal-to-octal'
    model['headerTitle'] = 'Strumento di conversione online da decimale a ottale  - Coding.Tools'
    model['bodyTitle'] = 'Strumento di conversione online da decimale a ottale'
    model['description'] = 'Questo strumento di conversione da decimale a ottale online ti aiuta a convertire un numero decimale in un numero ottale.'
    model['keywords'] = 'Da decimale a ottale, da decimale a ottale'
    model['image'] = '/image/cartoon-decimal-to-octal.png'
    return render_template(template_dir + 'template_decimal_to_octal_it.html', model=model)


@Web_HexToDecimal_blueprint.route('/it/binary-to-decimal')
def binary_to_decimal():
    model = get_default_model()
    model['url'] = '/it/binary-to-decimal'
    model['enUrl'] = '/binary-to-decimal'
    model['headerTitle'] = 'Strumento di conversione online da binario a decimale  - Coding.Tools'
    model['bodyTitle'] = 'Strumento di conversione online da binario a decimale'
    model['description'] = 'Questo strumento di conversione da binario online a decimale ti aiuta a convertire un numero ottale in un numero decimale.'
    model['keywords'] = 'Da binario a decimale, da binario a decimale'
    model['image'] = '/image/cartoon-decimal-to-binary.png'
    return render_template(template_dir + 'template_binary_to_decimal_it.html', model=model)


@Web_HexToDecimal_blueprint.route('/it/decimal-to-binary')
def decimal_to_binary():
    model = get_default_model()
    model['url'] = '/it/decimal-to-binary'
    model['enUrl'] = '/decimal-to-binary'
    model['headerTitle'] = 'Strumento di conversione da decimale a binario online  - Coding.Tools'
    model['bodyTitle'] = 'Strumento di conversione online da decimale a binario'
    model['description'] = 'Questo strumento decimale online per la conversione binaria consente di convertire un numero decimale in un numero binario.'
    model['keywords'] = 'Da decimale a binario, da decimale a binario'
    model['image'] = '/image/cartoon-decimal-to-binary.png'
    return render_template(template_dir + 'template_decimal_to_binary_it.html', model=model)


@Web_HexToDecimal_blueprint.route('/it/ascii-table')
def ascii_table():
    model = get_default_model()
    model['url'] = '/it/ascii-table'
    model['enUrl'] = '/ascii-table'
    model['headerTitle'] = 'Tabella di ricerca ASCII  - Coding.Tools'
    model['bodyTitle'] = 'Tabella di ricerca ASCII'
    model['description'] = 'Tabella di ricerca ASCII completa (256 bit), inclusi caratteri di controllo ASCII, simboli ASCII e caratteri ASCII estesi.'
    model['keywords'] = 'Tabella ASCII, tabella di estensione ASCII'
    model['image'] = '/image/logo.png'
    return render_template(template_dir + 'template_ascii_table_it.html', model=model)


@Web_HexToDecimal_blueprint.route('/it/hex-to-ascii')
def hex_to_ascii():
    model = get_default_model()
    model['url'] = '/it/hex-to-ascii'
    model['enUrl'] = '/hex-to-ascii'
    model['headerTitle'] = 'Strumento di conversione online con stringa esadecimale in ASCII  - Coding.Tools'
    model['bodyTitle'] = 'Strumento di conversione online con stringa esadecimale in ASCII'
    model['description'] = 'Questo strumento di conversione di stringhe esadecimali online in ASCII ti aiuta a convertire un array esadecimale in una stringa ASCII.'
    model['keywords'] = 'Esadecimale in ASCII, esadecimale in ASCII'
    model['image'] = '/image/cartoon-hex-to-ascii.png'
    return render_template(template_dir + 'template_hex_to_ascii_it.html', model=model)


@Web_HexToDecimal_blueprint.route('/it/ascii-to-hex')
def ascii_to_hex():
    model = get_default_model()
    model['url'] = '/it/ascii-to-hex'
    model['enUrl'] = '/ascii-to-hex'
    model['headerTitle'] = 'Stringa ASCII per strumento di conversione online esadecimale  - Coding.Tools'
    model['bodyTitle'] = 'Stringa ASCII allo strumento di conversione online esadecimale'
    model['description'] = 'Questa stringa ASCII online per strumento di conversione esadecimale ti aiuta a convertire una stringa ASCII in una matrice esadecimale.'
    model['keywords'] = 'ASCII in esadecimale, ASCII in esadecimale'
    model['image'] = '/image/cartoon-ascii-to-hex.png'
    return render_template(template_dir + 'template_ascii_to_hex_it.html', model=model)


@Web_HexToDecimal_blueprint.route('/it/fraction-to-decimal')
def fraction_to_decimal():
    model = get_default_model()
    model['url'] = '/it/fraction-to-decimal'
    model['enUrl'] = '/fraction-to-decimal'
    model['headerTitle'] = 'Punteggio per lo strumento di conversione online decimale  - Coding.Tools'
    model['bodyTitle'] = 'Punteggio per lo strumento di conversione online decimale'
    model['description'] = 'Questo strumento per la conversione da punteggio online a decimale ti aiuta a convertire un punteggio in un decimale Il numeratore e il denominatore di input sono visualizzati nella casella dei risultati.'
    model['keywords'] = 'Da frazione a decimale, da frazione a decimale'
    model['image'] = '/image/cartoon-fraction-to-decimal.png'
    return render_template(template_dir + 'template_fraction_to_decimal_it.html', model=model)


@Web_HexToDecimal_blueprint.route('/it/decimal-to-fraction')
def decimal_to_fraction():
    model = get_default_model()
    model['url'] = '/it/decimal-to-fraction'
    model['enUrl'] = '/decimal-to-fraction'
    model['headerTitle'] = 'Strumento di conversione in linea decimale per segnare  - Coding.Tools'
    model['bodyTitle'] = 'Decimale per segnare lo strumento di conversione online'
    model['description'] = 'Questo strumento decimale per la conversione dei punteggi decimale online ti aiuta a convertire un decimale in un punteggio. Inserisci il decimale e il punteggio verrà visualizzato nella casella dei risultati.'
    model['keywords'] = 'Da decimale a frazione, da frazione a frazione'
    model['image'] = '/image/cartoon-decimal-to-fraction.png'
    return render_template(template_dir + 'template_decimal_to_fraction_it.html', model=model)


@Web_HexToDecimal_blueprint.route('/it/percent-to-decimal')
def percent_to_decimal():
    model = get_default_model()
    model['url'] = '/it/percent-to-decimal'
    model['enUrl'] = '/percent-to-decimal'
    model['headerTitle'] = 'Strumento di conversione online da percentuale a decimale  - Coding.Tools'
    model['bodyTitle'] = 'Strumento di conversione online da percentuale a decimale'
    model['description'] = 'Questo strumento di conversione da percentuale online a decimale ti aiuta a convertire una percentuale in un decimale. Inserisci una percentuale e il decimale comparirà nella casella dei risultati.'
    model['keywords'] = 'Da percentuale a decimale, da percentuale a decimale'
    model['image'] = '/image/cartoon-percent-to-decimal.png'
    return render_template(template_dir + 'template_percent_to_decimal_it.html', model=model)


@Web_HexToDecimal_blueprint.route('/it/decimal-to-percent')
def decimal_to_percent():
    model = get_default_model()
    model['url'] = '/it/decimal-to-percent'
    model['enUrl'] = '/decimal-to-percent'
    model['headerTitle'] = 'Strumento di conversione online decimale in percentuale  - Coding.Tools'
    model['bodyTitle'] = 'Strumento di conversione online decimale in percentuale'
    model['description'] = 'Questo strumento di conversione decimale in percentuale online ti aiuta a convertire un decimale in percentuale. Inserisci il decimale e la percentuale verrà visualizzata nella casella dei risultati.'
    model['keywords'] = 'Da decimale a percentuale, da frazione a percentuale'
    model['image'] = '/image/cartoon-decimal-to-percent.png'
    return render_template(template_dir + 'template_decimal_to_percent_it.html', model=model)


@Web_HexToDecimal_blueprint.route('/it/percent-to-fraction')
def percent_to_fraction():
    model = get_default_model()
    model['url'] = '/it/percent-to-fraction'
    model['enUrl'] = '/percent-to-fraction'
    model['headerTitle'] = 'Percentuale per ottenere lo strumento di conversione online  - Coding.Tools'
    model['bodyTitle'] = 'Percentuale per ottenere lo strumento di conversione online'
    model['description'] = 'Questa percentuale online per lo strumento di conversione dei punteggi ti aiuta a convertire una percentuale in un punteggio. Inserisci la percentuale e il punteggio verrà visualizzato nella casella dei risultati.'
    model['keywords'] = 'Percentuale alla frazione, percentuale alla frazione'
    model['image'] = '/image/cartoon-percent-to-fraction.png'
    return render_template(template_dir + 'template_percent_to_fraction_it.html', model=model)


@Web_HexToDecimal_blueprint.route('/it/fraction-to-percent')
def fraction_to_percent():
    model = get_default_model()
    model['url'] = '/it/fraction-to-percent'
    model['enUrl'] = '/fraction-to-percent'
    model['headerTitle'] = 'Punteggio per strumento di conversione online in percentuale  - Coding.Tools'
    model['bodyTitle'] = 'Punteggio sullo strumento di conversione online percentuale'
    model['description'] = 'Questo strumento per la valutazione del punteggio in percentuale consente di convertire un punteggio in percentuale. Immettere il numeratore e il denominatore e la percentuale verrà visualizzata nella casella dei risultati.'
    model['keywords'] = 'Frazione in percentuale, percentuale frazionaria'
    model['image'] = '/image/cartoon-fraction-to-percent.png'
    return render_template(template_dir + 'template_fraction_to_percent_it.html', model=model)


@Web_HexToDecimal_blueprint.route('/it/hex-to-rgb')
def hex_to_rgb():
    model = get_default_model()
    model['url'] = '/it/hex-to-rgb'
    model['enUrl'] = '/hex-to-rgb'
    model['headerTitle'] = 'Strumento di conversione in linea di colore esadecimale a colore RGB  - Coding.Tools'
    model['bodyTitle'] = 'Strumento di conversione in linea di colore esadecimale in colore RGB'
    model['description'] = 'Questo strumento per la conversione dei colori RGB esadecimale colore online ti aiuta a convertire un colore esadecimale in un colore RGB e a testare il colore prescelto in tempo reale.'
    model['keywords'] = 'Da esadecimale a RGB, da colore esadecimale a RGB'
    model['image'] = '/image/cartoon-hex-to-rgb.png'
    return render_template(template_dir + 'template_hex_to_rgb_it.html', model=model)


@Web_HexToDecimal_blueprint.route('/it/rgb-to-hex')
def rgb_to_hex():
    model = get_default_model()
    model['url'] = '/it/rgb-to-hex'
    model['enUrl'] = '/rgb-to-hex'
    model['headerTitle'] = 'Strumento di conversione online da Colore RGB a Colore esagonale  - Coding.Tools'
    model['bodyTitle'] = 'Strumento di conversione online a colori esadecimali RGB'
    model['description'] = 'Questo strumento per la conversione del colore esadecimale a colori da RGB a online ti aiuta a convertire un colore RGB in un colore esadecimale e a testare il colore prescelto in tempo reale.'
    model['keywords'] = 'Da RGB a esadecimale, da colore RGB a colore esadecimale'
    model['image'] = '/image/cartoon-rgb-to-hex.png'
    return render_template(template_dir + 'template_rgb_to_hex_it.html', model=model)


@Web_HexToDecimal_blueprint.route('/it/hex-to-rgba')
def hex_to_rgba():
    model = get_default_model()
    model['url'] = '/it/hex-to-rgba'
    model['enUrl'] = '/hex-to-rgba'
    model['headerTitle'] = 'Strumento di conversione online a colori esadecimali RGBA  - Coding.Tools'
    model['bodyTitle'] = 'Strumento di conversione online a colori RGBA colore esadecimale'
    model['description'] = 'Questo strumento per la conversione dei colori RGB esadecimale colore online consente di convertire un colore esadecimale in un colore RGBA (inclusa Opacità trasparenza) e di testare il colore prescelto in tempo reale.'
    model['keywords'] = 'Da esadecimale a RGBA, colore esadecimale a colore RGBA'
    model['image'] = '/image/cartoon-hex-to-rgba.png'
    return render_template(template_dir + 'template_hex_to_rgba_it.html', model=model)


@Web_HexToDecimal_blueprint.route('/it/rgba-to-hex')
def rgba_to_hex():
    model = get_default_model()
    model['url'] = '/it/rgba-to-hex'
    model['enUrl'] = '/rgba-to-hex'
    model['headerTitle'] = 'Strumento di conversione online a colori esadecimale colore RGBA  - Coding.Tools'
    model['bodyTitle'] = 'Strumento di conversione online a colori esadecimale colore RGBA'
    model['description'] = 'Questo strumento per la conversione del colore esadecimale a colori da RGBA a colore aiuta a convertire un colore RGBA (inclusa Opacità trasparenza) in colore esadecimale e a testare il colore prescelto in tempo reale.'
    model['keywords'] = 'Da RGBA a esadecimale, da colore RGBA a colore esadecimale'
    model['image'] = '/image/cartoon-rgba-to-hex.png'
    return render_template(template_dir + 'template_rgba_to_hex_it.html', model=model)


@Web_HexToDecimal_blueprint.route('/it/roman-numerals-chart')
def roman_numerals_chart():
    model = get_default_model()
    model['url'] = '/it/roman-numerals-chart'
    model['enUrl'] = '/roman-numerals-chart'
    model['headerTitle'] = 'Tabella dei numeri romani 1-1000  - Coding.Tools'
    model['bodyTitle'] = 'Tabella di confronto numeri romani 1-1000'
    model['description'] = 'Una tabella di confronto dei numeri romani completa da 1 a 1000.'
    model['keywords'] = 'Grafico a numeri romani, numeri romani'
    model['image'] = '/image/logo.png'
    return render_template(template_dir + 'template_roman_numerals_chart_it.html', model=model)


@Web_HexToDecimal_blueprint.route('/it/roman-numerals-to-numbers')
def roman_numerals_to_numbers():
    model = get_default_model()
    model['url'] = '/it/roman-numerals-to-numbers'
    model['enUrl'] = '/roman-numerals-to-numbers'
    model['headerTitle'] = 'Strumento di conversione online di numeri romani in numeri arabi  - Coding.Tools'
    model['bodyTitle'] = 'Numero romano allo strumento di conversione online digitale arabo'
    model['description'] = 'Questo strumento per la conversione dei numeri arabi in linea dei numeri romani ti aiuta a convertire un numero romano in un numero arabo. Inserisci il numero romano e il numero arabo verrà visualizzato nella casella dei risultati.'
    model['keywords'] = 'I numeri romani diventano numeri arabi'
    model['image'] = '/image/cartoon-roman-numerals-to-numbers.png'
    return render_template(template_dir + 'template_roman_numerals_to_numbers_it.html', model=model)


@Web_HexToDecimal_blueprint.route('/it/numbers-to-roman-numerals')
def numbers_to_roman_numerals():
    model = get_default_model()
    model['url'] = '/it/numbers-to-roman-numerals'
    model['enUrl'] = '/numbers-to-roman-numerals'
    model['headerTitle'] = 'Strumento di conversione online da digitale digitale a romano digitale  - Coding.Tools'
    model['bodyTitle'] = 'Strumento di conversione online da digitale digitale a romano digitale'
    model['description'] = 'Questo strumento numerico online per lo strumento di conversione dei numeri romani ti aiuta a convertire un numero arabo in un numero romano. Inserisci il numero arabo e il numero romano verrà visualizzato nella casella dei risultati.'
    model['keywords'] = 'Le cifre arabe diventano numeri romani'
    model['image'] = '/image/cartoon-numbers-to-roman-numerals.png'
    return render_template(template_dir + 'template_numbers_to_roman_numerals_it.html', model=model)

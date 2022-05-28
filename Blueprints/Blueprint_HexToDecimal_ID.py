from flask import Blueprint, render_template
from Logic import Logic_UTIL, Logic_Config, Logic_MyIpAddress

Web_HexToDecimal_blueprint = Blueprint('Web_HexToDecimal_blueprint_ID', __name__)
template_dir = 'HexToDecimal/id/'

def get_default_model():
    model = Logic_UTIL.create_default_model()
    model['clientIP'] = Logic_MyIpAddress.public_ip_address_api()
    model['lang'] = 'id'
    return model

@Web_HexToDecimal_blueprint.route('/id/hex-to-decimal')
def hex_to_decimal():
    model = get_default_model()
    model['url'] = '/id/hex-to-decimal'
    model['enUrl'] = '/hex-to-decimal'
    model['headerTitle'] = 'Alat Konversi Heksadesimal ke Desimal  - Coding.Tools'
    model['bodyTitle'] = 'Alat konversi online heksadesimal ke desimal'
    model['description'] = 'Alat konversi heksadesimal ke desimal online ini membantu Anda mengonversi angka heksadesimal menjadi angka desimal.'
    model['keywords'] = 'Hex ke Desimal, hexadecimal ke desimal'
    model['image'] = '/image/cartoon-hex-to-decimal.png'
    return render_template(template_dir + 'template_hex_to_decimal_id.html', model=model)


@Web_HexToDecimal_blueprint.route('/id/decimal-to-hex')
def decimal_to_hex():
    model = get_default_model()
    model['url'] = '/id/decimal-to-hex'
    model['enUrl'] = '/decimal-to-hex'
    model['headerTitle'] = 'Alat konversi online desimal ke heksadesimal  - Coding.Tools'
    model['bodyTitle'] = 'Alat konversi online desimal ke heksadesimal'
    model['description'] = 'Alat konversi desimal ke hex online ini membantu Anda mengonversi angka desimal menjadi angka heksadesimal.'
    model['keywords'] = 'Desimal ke Hex, desimal ke heksadesimal'
    model['image'] = '/image/cartoon-decimal-to-hex.png'
    return render_template(template_dir + 'template_decimal_to_hex_id.html', model=model)


@Web_HexToDecimal_blueprint.route('/id/octal-to-decimal')
def octal_to_decimal():
    model = get_default_model()
    model['url'] = '/id/octal-to-decimal'
    model['enUrl'] = '/octal-to-decimal'
    model['headerTitle'] = 'Oktal ke Desimal Alat Konversi Online  - Coding.Tools'
    model['bodyTitle'] = 'Oktal ke alat desimal konversi online'
    model['description'] = 'Alat konversi oktal ke desimal online ini membantu Anda mengonversi angka oktal ke angka desimal.'
    model['keywords'] = 'Oktal ke Desimal, oktal ke desimal'
    model['image'] = '/image/octal_to_decimal.png'
    return render_template(template_dir + 'template_octal_to_decimal_id.html', model=model)


@Web_HexToDecimal_blueprint.route('/id/decimal-to-octal')
def decimal_to_octal():
    model = get_default_model()
    model['url'] = '/id/decimal-to-octal'
    model['enUrl'] = '/decimal-to-octal'
    model['headerTitle'] = 'Alat Konversi Online Desimal ke Oktal  - Coding.Tools'
    model['bodyTitle'] = 'Alat konversi online desimal ke oktal'
    model['description'] = 'Alat konversi desimal ke oktal online ini membantu Anda mengubah angka desimal menjadi angka oktal.'
    model['keywords'] = 'Desimal ke Oktal, desimal ke oktal'
    model['image'] = '/image/cartoon-decimal-to-octal.png'
    return render_template(template_dir + 'template_decimal_to_octal_id.html', model=model)


@Web_HexToDecimal_blueprint.route('/id/binary-to-decimal')
def binary_to_decimal():
    model = get_default_model()
    model['url'] = '/id/binary-to-decimal'
    model['enUrl'] = '/binary-to-decimal'
    model['headerTitle'] = 'Alat konversi biner ke desimal online  - Coding.Tools'
    model['bodyTitle'] = 'Alat konversi online biner ke desimal'
    model['description'] = 'Alat konversi biner ke desimal online ini membantu Anda mengonversi angka oktal ke angka desimal.'
    model['keywords'] = 'Biner ke Desimal, biner ke desimal'
    model['image'] = '/image/cartoon-decimal-to-binary.png'
    return render_template(template_dir + 'template_binary_to_decimal_id.html', model=model)


@Web_HexToDecimal_blueprint.route('/id/decimal-to-binary')
def decimal_to_binary():
    model = get_default_model()
    model['url'] = '/id/decimal-to-binary'
    model['enUrl'] = '/decimal-to-binary'
    model['headerTitle'] = 'Alat konversi desimal ke biner online  - Coding.Tools'
    model['bodyTitle'] = 'Alat konversi desimal ke biner online'
    model['description'] = 'Alat konversi desimal ke biner online ini membantu Anda mengonversi angka desimal ke angka biner.'
    model['keywords'] = 'Desimal ke Biner, desimal ke biner'
    model['image'] = '/image/cartoon-decimal-to-binary.png'
    return render_template(template_dir + 'template_decimal_to_binary_id.html', model=model)


@Web_HexToDecimal_blueprint.route('/id/ascii-table')
def ascii_table():
    model = get_default_model()
    model['url'] = '/id/ascii-table'
    model['enUrl'] = '/ascii-table'
    model['headerTitle'] = 'Tabel pencarian ASCII  - Coding.Tools'
    model['bodyTitle'] = 'Tabel pencarian ASCII'
    model['description'] = 'Tabel pencarian ASCII lengkap (256 bit), termasuk karakter kontrol ASCII, simbol ASCII, dan karakter tambahan ASCII.'
    model['keywords'] = 'Tabel ASCII, tabel ekstensi ASCII'
    model['image'] = '/image/logo.png'
    return render_template(template_dir + 'template_ascii_table_id.html', model=model)


@Web_HexToDecimal_blueprint.route('/id/hex-to-ascii')
def hex_to_ascii():
    model = get_default_model()
    model['url'] = '/id/hex-to-ascii'
    model['enUrl'] = '/hex-to-ascii'
    model['headerTitle'] = 'Alat konversi online heksadesimal ke ASCII  - Coding.Tools'
    model['bodyTitle'] = 'Alat konversi online string heksadesimal ke ASCII'
    model['description'] = 'Alat konversi string heksadesimal ke ASCII online ini membantu Anda mengonversi array heksadesimal menjadi string ASCII.'
    model['keywords'] = 'Hex ke ASCII, hex ke ASCII'
    model['image'] = '/image/cartoon-hex-to-ascii.png'
    return render_template(template_dir + 'template_hex_to_ascii_id.html', model=model)


@Web_HexToDecimal_blueprint.route('/id/ascii-to-hex')
def ascii_to_hex():
    model = get_default_model()
    model['url'] = '/id/ascii-to-hex'
    model['enUrl'] = '/ascii-to-hex'
    model['headerTitle'] = 'String ASCII ke alat konversi online heksadesimal  - Coding.Tools'
    model['bodyTitle'] = 'String ASCII ke alat konversi online heksadesimal'
    model['description'] = 'Alat ASCII string ke hex konversi online ini membantu Anda mengkonversi string ASCII ke array heksadesimal.'
    model['keywords'] = 'ASCII ke Hex, ASCII ke hexadecimal'
    model['image'] = '/image/cartoon-ascii-to-hex.png'
    return render_template(template_dir + 'template_ascii_to_hex_id.html', model=model)


@Web_HexToDecimal_blueprint.route('/id/fraction-to-decimal')
def fraction_to_decimal():
    model = get_default_model()
    model['url'] = '/id/fraction-to-decimal'
    model['enUrl'] = '/fraction-to-decimal'
    model['headerTitle'] = 'Skor ke alat konversi online desimal  - Coding.Tools'
    model['bodyTitle'] = 'Skor ke alat konversi online desimal'
    model['description'] = 'Alat konversi skor ke desimal online ini membantu Anda mengonversi skor menjadi desimal. Pembilang input dan penyebut ditampilkan di kotak hasil.'
    model['keywords'] = 'Fraksi ke Desimal, Fraksional ke Desimal'
    model['image'] = '/image/cartoon-fraction-to-decimal.png'
    return render_template(template_dir + 'template_fraction_to_decimal_id.html', model=model)


@Web_HexToDecimal_blueprint.route('/id/decimal-to-fraction')
def decimal_to_fraction():
    model = get_default_model()
    model['url'] = '/id/decimal-to-fraction'
    model['enUrl'] = '/decimal-to-fraction'
    model['headerTitle'] = 'Desimal untuk mencetak alat konversi online  - Coding.Tools'
    model['bodyTitle'] = 'Desimal untuk mencetak alat konversi online'
    model['description'] = 'Alat konversi desimal ke skor daring ini membantu Anda mengonversi desimal menjadi fraksi. Masukkan desimal dan skor akan ditampilkan di kotak hasil.'
    model['keywords'] = 'Desimal ke Fraksi, fraksional ke Fraksi'
    model['image'] = '/image/cartoon-decimal-to-fraction.png'
    return render_template(template_dir + 'template_decimal_to_fraction_id.html', model=model)


@Web_HexToDecimal_blueprint.route('/id/percent-to-decimal')
def percent_to_decimal():
    model = get_default_model()
    model['url'] = '/id/percent-to-decimal'
    model['enUrl'] = '/percent-to-decimal'
    model['headerTitle'] = 'Persentase ke alat konversi online desimal  - Coding.Tools'
    model['bodyTitle'] = 'Persentase ke alat konversi online desimal'
    model['description'] = 'Alat konversi persentase ke desimal online ini membantu Anda mengonversi persentase menjadi desimal. Masukkan persentase dan desimal akan muncul di kotak hasil.'
    model['keywords'] = 'Persen ke Desimal, persentase ke desimal'
    model['image'] = '/image/cartoon-percent-to-decimal.png'
    return render_template(template_dir + 'template_percent_to_decimal_id.html', model=model)


@Web_HexToDecimal_blueprint.route('/id/decimal-to-percent')
def decimal_to_percent():
    model = get_default_model()
    model['url'] = '/id/decimal-to-percent'
    model['enUrl'] = '/decimal-to-percent'
    model['headerTitle'] = 'Desimal ke persentase alat konversi online  - Coding.Tools'
    model['bodyTitle'] = 'Alat konversi online desimal ke persentase'
    model['description'] = 'Alat konversi desimal ke persentase daring ini membantu Anda mengonversi desimal menjadi persentase. Masukkan desimal dan persentase akan ditampilkan di kotak hasil.'
    model['keywords'] = 'Desimal ke Persen, fraksional ke persentase'
    model['image'] = '/image/cartoon-decimal-to-percent.png'
    return render_template(template_dir + 'template_decimal_to_percent_id.html', model=model)


@Web_HexToDecimal_blueprint.route('/id/percent-to-fraction')
def percent_to_fraction():
    model = get_default_model()
    model['url'] = '/id/percent-to-fraction'
    model['enUrl'] = '/percent-to-fraction'
    model['headerTitle'] = 'Persentase ke Skor Alat Konversi Online  - Coding.Tools'
    model['bodyTitle'] = 'Persentase untuk mencetak alat konversi online'
    model['description'] = 'Alat konversi persentase ke skor daring ini membantu Anda mengonversi persentase menjadi skor. Masukkan persentase dan skor akan ditampilkan di kotak hasil.'
    model['keywords'] = 'Persen ke Fraksi, Persentase ke Fraksi'
    model['image'] = '/image/cartoon-percent-to-fraction.png'
    return render_template(template_dir + 'template_percent_to_fraction_id.html', model=model)


@Web_HexToDecimal_blueprint.route('/id/fraction-to-percent')
def fraction_to_percent():
    model = get_default_model()
    model['url'] = '/id/fraction-to-percent'
    model['enUrl'] = '/fraction-to-percent'
    model['headerTitle'] = 'Skor ke persentase alat konversi online  - Coding.Tools'
    model['bodyTitle'] = 'Skor ke persentase alat konversi online'
    model['description'] = 'Alat konversi skor ke persentase online ini membantu Anda mengonversi skor menjadi persentase. Masukkan pembilang dan penyebut dan persentase akan ditampilkan di kotak hasil.'
    model['keywords'] = 'Fraksi ke Persen, persentase fraksional'
    model['image'] = '/image/cartoon-fraction-to-percent.png'
    return render_template(template_dir + 'template_fraction_to_percent_id.html', model=model)


@Web_HexToDecimal_blueprint.route('/id/hex-to-rgb')
def hex_to_rgb():
    model = get_default_model()
    model['url'] = '/id/hex-to-rgb'
    model['enUrl'] = '/hex-to-rgb'
    model['headerTitle'] = 'Alat Konversi Daring Warna Hex ke RGB Color  - Coding.Tools'
    model['bodyTitle'] = 'Alat konversi online Hex color ke RGB color'
    model['description'] = 'Alat konversi warna Hex ke RGB warna ini membantu Anda mengonversi warna Hex menjadi warna RGB dan menguji warna pilihan Anda secara real time.'
    model['keywords'] = 'Hex ke RGB, Hex warna ke warna RGB'
    model['image'] = '/image/cartoon-hex-to-rgb.png'
    return render_template(template_dir + 'template_hex_to_rgb_id.html', model=model)


@Web_HexToDecimal_blueprint.route('/id/rgb-to-hex')
def rgb_to_hex():
    model = get_default_model()
    model['url'] = '/id/rgb-to-hex'
    model['enUrl'] = '/rgb-to-hex'
    model['headerTitle'] = 'Alat Konversi Daring Warna RGB ke Hex Color  - Coding.Tools'
    model['bodyTitle'] = 'Alat konversi online warna RGB ke Hex color'
    model['description'] = 'Alat konversi warna RGB ke Hex warna online ini membantu Anda mengubah warna RGB menjadi warna Hex dan menguji warna pilihan Anda secara real time.'
    model['keywords'] = 'RGB ke Hex, warna RGB ke warna Hex'
    model['image'] = '/image/cartoon-rgb-to-hex.png'
    return render_template(template_dir + 'template_rgb_to_hex_id.html', model=model)


@Web_HexToDecimal_blueprint.route('/id/hex-to-rgba')
def hex_to_rgba():
    model = get_default_model()
    model['url'] = '/id/hex-to-rgba'
    model['enUrl'] = '/hex-to-rgba'
    model['headerTitle'] = 'Alat Konversi Online Hex Color ke RGBA Color  - Coding.Tools'
    model['bodyTitle'] = 'Hex warna ke alat konversi online warna RGBA'
    model['description'] = 'Alat konversi warna Hex ke RGBA online ini membantu Anda mengubah warna Hex menjadi warna RGBA (termasuk transparansi Opacity) dan menguji warna pilihan Anda secara real time.'
    model['keywords'] = 'Hex ke RGBA, Hex warna ke warna RGBA'
    model['image'] = '/image/cartoon-hex-to-rgba.png'
    return render_template(template_dir + 'template_hex_to_rgba_id.html', model=model)


@Web_HexToDecimal_blueprint.route('/id/rgba-to-hex')
def rgba_to_hex():
    model = get_default_model()
    model['url'] = '/id/rgba-to-hex'
    model['enUrl'] = '/rgba-to-hex'
    model['headerTitle'] = 'Warna RGBA ke alat konversi online warna Hex  - Coding.Tools'
    model['bodyTitle'] = 'Alat konversi online warna RGBA ke Hex color'
    model['description'] = 'Alat konversi warna RGBA ke Hex warna online ini membantu Anda mengonversi warna RGBA (termasuk transparansi Opacity) ke warna Hex dan menguji warna pilihan Anda secara real time.'
    model['keywords'] = 'RGBA ke Hex, warna RGBA ke warna Hex'
    model['image'] = '/image/cartoon-rgba-to-hex.png'
    return render_template(template_dir + 'template_rgba_to_hex_id.html', model=model)


@Web_HexToDecimal_blueprint.route('/id/roman-numerals-chart')
def roman_numerals_chart():
    model = get_default_model()
    model['url'] = '/id/roman-numerals-chart'
    model['enUrl'] = '/roman-numerals-chart'
    model['headerTitle'] = 'Tabel angka Romawi 1-1000  - Coding.Tools'
    model['bodyTitle'] = 'Tabel perbandingan angka Romawi 1-1000'
    model['description'] = 'Tabel perbandingan angka Romawi lengkap dari 1 hingga 1000.'
    model['keywords'] = 'Grafik Angka Romawi, Angka Romawi'
    model['image'] = '/image/logo.png'
    return render_template(template_dir + 'template_roman_numerals_chart_id.html', model=model)


@Web_HexToDecimal_blueprint.route('/id/roman-numerals-to-numbers')
def roman_numerals_to_numbers():
    model = get_default_model()
    model['url'] = '/id/roman-numerals-to-numbers'
    model['enUrl'] = '/roman-numerals-to-numbers'
    model['headerTitle'] = 'Alat konversi online angka romawi ke angka arab  - Coding.Tools'
    model['bodyTitle'] = 'Alat konversi angka digital ke Arab secara online'
    model['description'] = 'Alat konversi angka Romawi ke Arab online ini membantu Anda mengonversi angka Romawi menjadi angka Arab. Masukkan angka Romawi dan angka Arab akan ditampilkan di kotak hasil.'
    model['keywords'] = 'Angka Romawi beralih ke angka Arab'
    model['image'] = '/image/cartoon-roman-numerals-to-numbers.png'
    return render_template(template_dir + 'template_roman_numerals_to_numbers_id.html', model=model)


@Web_HexToDecimal_blueprint.route('/id/numbers-to-roman-numerals')
def numbers_to_roman_numerals():
    model = get_default_model()
    model['url'] = '/id/numbers-to-roman-numerals'
    model['enUrl'] = '/numbers-to-roman-numerals'
    model['headerTitle'] = 'Digital Arab ke Roman Digital Conversion Tool  - Coding.Tools'
    model['bodyTitle'] = 'Alat Konversi Online Digital Arab ke Romawi Digital'
    model['description'] = 'Alat konversi bilangan Arab ke Romawi online ini membantu Anda mengonversi angka Arab ke angka Romawi. Masukkan nomor Arab dan angka Romawi akan ditampilkan di kotak hasil.'
    model['keywords'] = 'Angka Arab beralih ke angka Romawi'
    model['image'] = '/image/cartoon-numbers-to-roman-numerals.png'
    return render_template(template_dir + 'template_numbers_to_roman_numerals_id.html', model=model)

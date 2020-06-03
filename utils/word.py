import os

from docx import Document
from docx.shared import Pt


def word_skzi(request, skzis):
    doc = Document('static/files/obrazets_prilozhenie_14.1.docx')
    table = doc.tables[0]
    for i, skzi in enumerate(skzis):
        table.add_row()
        row = i+3
        table.cell(row, 0).text = str(i+1)
        table.cell(row, 1).text = str(skzi.name)
        table.cell(row, 2).text = skzi.serial_n
        table.cell(row, 3).text = skzi.ekz_n
        table.cell(row, 4).text = str(skzi.from_organ)
        l = []
        if skzi.date_poluch:
            l.append(skzi.date_poluch.strftime('%d.%m.%Y'))
        if skzi.nomer_poluch:
            l.append(skzi.nomer_poluch)
        table.cell(row, 5).text = ', '.join(l)

        table.cell(row, 6).text = skzi.to_person.get_fio()
        l = []
        if skzi.date_sopr:
            l.append(skzi.date_sopr.strftime('%d.%m.%Y'))
        if skzi.nomer_sopr:
            l.append(skzi.nomer_sopr)
        table.cell(row, 7).text = ', '.join(l)
        l = []
        if skzi.date_podtv:
            l.append(skzi.date_podtv.strftime('%d.%m.%Y'))
        if skzi.nomer_podtv:
            l.append(skzi.nomer_podtv)
        table.cell(row, 7).text = ', '.join(l)
        l = []
        if skzi.vozvr_date_sopr:
            l.append(skzi.vozvr_date_sopr.strftime('%d.%m.%Y'))
        if skzi.vozvr_nomer_sopr:
            l.append(skzi.vozvr_nomer_sopr)
        table.cell(row, 8).text = ', '.join(l)
        l = []
        if skzi.vozvr_date_podtv:
            l.append(skzi.vozvr_date_podtv.strftime('%d.%m.%Y'))
        if skzi.vozvr_nomer_podtv:
            l.append(skzi.vozvr_nomer_podtv)
        table.cell(row, 9).text = ', '.join(l)

        if skzi.date_vvod:
            table.cell(row, 10).text = skzi.date_vvod.strftime('%d.%m.%Y')
        if skzi.date_vivod:
            table.cell(row, 11).text = skzi.date_vivod.strftime('%d.%m.%Y')
        if skzi.date_unichtozh:
            table.cell(row, 12).text = skzi.date_unichtozh.strftime('%d.%m.%Y')
        if skzi.nomer_acta:
            table.cell(row, 13).text = skzi.nomer_acta
        if skzi.primechanie:
            table.cell(row, 14).text = skzi.primechanie



    for row in table.rows:
        for cell in row.cells:
            paragraphs = cell.paragraphs
            for paragraph in paragraphs:
                for run in paragraph.runs:
                    font = run.font
                    font.size = Pt(9)

    path = f'tmp/skzi/word/{request.user.id}'

    if not os.path.exists(path):
        os.makedirs(path)

    filename = f'Журнал СКЗИ.docx'
    path += f'/{filename}'

    doc.save(path)
    return path
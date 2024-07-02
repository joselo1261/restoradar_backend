from flask import Flask, request, send_file
from app import app,db,ma
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

@app.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    data = request.json['datosFiltrados']

    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    y = height - 40

    for item in data:
        text = f"{item['properties']['nombre']}: {item['properties']['categoria']}, {item['properties']['cocina']}, {item['properties']['barrio']}"
        pdf.drawString(30, y, text)
        y -= 20
        if y < 40:
            pdf.showPage()
            y = height - 40

    pdf.save()
    buffer.seek(0)

    return send_file(buffer, as_attachment=True, download_name='listado_gastronomico_caba.pdf', mimetype='application/pdf')


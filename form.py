import flet as ft
import csv
import os

CSV_FILE = "registration_data.csv"

def main(page: ft.Page):
    page.title = "แบบฟอร์มรับสมัคร"
    page.window_width = 400
    page.window_height = 300

    # Input fields
    name_input = ft.TextField(label="ชื่อ-สกุล", width=300)
    phone_input = ft.TextField(label="หมายเลขโทรศัพท์", width=300, keyboard_type=ft.KeyboardType.PHONE)
    team_input = ft.TextField(label="ชื่อทีม", width=300)

    result_text = ft.Text()

    # Save function
    def save_to_csv(e):
        name = name_input.value.strip()
        phone = phone_input.value.strip()
        team = team_input.value.strip()

        if not name or not phone or not team:
            result_text.value = "กรุณากรอกข้อมูลให้ครบถ้วน"
            result_text.color = "red"
            page.update()
            return

        # สร้างไฟล์ csv ถ้ายังไม่มี และเขียน header
        file_exists = os.path.isfile(CSV_FILE)
        with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["ชื่อ-สกุล", "หมายเลขโทรศัพท์", "ชื่อทีม"])
            writer.writerow([name, phone, team])

        result_text.value = "✅ บันทึกข้อมูลเรียบร้อยแล้ว"
        result_text.color = "green"
        name_input.value = ""
        phone_input.value = ""
        team_input.value = ""
        page.update()

    # Layout
    page.add(
        ft.Column(
            controls=[
                name_input,
                phone_input,
                team_input,
                ft.ElevatedButton("บันทึก", on_click=save_to_csv),
                result_text
            ],
            spacing=10,
        )
    )

ft.app(target=main)

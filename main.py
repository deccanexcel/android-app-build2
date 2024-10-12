#good going
import flet as ft

def main(page: ft.Page):
    # Create form fields
    name_field = ft.TextField(label="Name", width=300)
    age_field = ft.TextField(label="Age", width=300)
    gender_field = ft.Dropdown(
        label="Gender", 
        options=[ft.dropdown.Option("Male"), ft.dropdown.Option("Female"), ft.dropdown.Option("Other")]
    )
    
    # Submit button
    def on_submit(e):
        # Show dialog with form data
        form_data = f"Name: {name_field.value}\nAge: {age_field.value}\nGender: {gender_field.value}"
        page.dialog = ft.AlertDialog(content=ft.Text(form_data))
        page.dialog.open = True
        page.update()
    
    submit_button = ft.ElevatedButton(text="Submit", on_click=on_submit)

    # Add form fields and submit button to the page
    page.add(
        ft.Column([
            name_field,
            age_field,
            gender_field,
            submit_button
        ])
    )

ft.app(target=main)

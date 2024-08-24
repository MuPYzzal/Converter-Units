import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox

class UnitConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Unit Converter')

        self.setGeometry(100, 100, 400, 200)

        # Layout
        layout = QVBoxLayout()

        # Conversion Type
        self.conversion_type = QComboBox(self)
        self.conversion_type.addItems(["Length", "Weight", "Temperature"])
        self.conversion_type.currentIndexChanged.connect(self.update_units)
        layout.addWidget(QLabel("Select Conversion Type:"))
        layout.addWidget(self.conversion_type)

        # Input Value
        layout.addWidget(QLabel("Enter value:"))
        self.input_value = QLineEdit(self)
        layout.addWidget(self.input_value)

        # Units ComboBoxes
        self.unit_from = QComboBox(self)
        self.unit_to = QComboBox(self)
        layout.addWidget(QLabel("From Unit:"))
        layout.addWidget(self.unit_from)
        layout.addWidget(QLabel("To Unit:"))
        layout.addWidget(self.unit_to)
        self.update_units()

        # Convert Button
        self.convert_button = QPushButton("Convert", self)
        self.convert_button.clicked.connect(self.convert)
        layout.addWidget(self.convert_button)

        # Output Value
        layout.addWidget(QLabel("Converted value:"))
        self.output_value = QLineEdit(self)
        self.output_value.setReadOnly(True)
        layout.addWidget(self.output_value)

        self.setLayout(layout)

    def update_units(self):
        conversion_type = self.conversion_type.currentText()

        if conversion_type == "Length":
            units = ["Meters", "Kilometers"]
        elif conversion_type == "Weight":
            units = ["Grams", "Kilograms"]
        elif conversion_type == "Temperature":
            units = ["Celsius", "Fahrenheit"]

        self.unit_from.clear()
        self.unit_to.clear()
        self.unit_from.addItems(units)
        self.unit_to.addItems(units)

    def convert(self):
        value = float(self.input_value.text())
        unit_from = self.unit_from.currentText()
        unit_to = self.unit_to.currentText()
        conversion_type = self.conversion_type.currentText()

        if conversion_type == "Length":
            result = self.convert_length(value, unit_from, unit_to)
        elif conversion_type == "Weight":
            result = self.convert_weight(value, unit_from, unit_to)
        elif conversion_type == "Temperature":
            result = self.convert_temperature(value, unit_from, unit_to)

        self.output_value.setText(str(result))

    def convert_length(self, value, unit_from, unit_to):
        if unit_from == "Meters" and unit_to == "Kilometers":
            return value / 1000
        elif unit_from == "Kilometers" and unit_to == "Meters":
            return value * 1000
        return value

    def convert_weight(self, value, unit_from, unit_to):
        if unit_from == "Grams" and unit_to == "Kilograms":
            return value / 1000
        elif unit_from == "Kilograms" and unit_to == "Grams":
            return value * 1000
        return value

    def convert_temperature(self, value, unit_from, unit_to):
        if unit_from == "Celsius" and unit_to == "Fahrenheit":
            return (value * 9/5) + 32
        elif unit_from == "Fahrenheit" and unit_to == "Celsius":
            return (value - 32) * 5/9
        return value

if __name__ == '__main__':
    app = QApplication(sys.argv)
    converter = UnitConverter()
    converter.show()
    sys.exit(app.exec_())
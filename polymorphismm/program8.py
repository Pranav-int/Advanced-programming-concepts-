# Q8. Create Report with generate().
# Derive PDFReport, ExcelReport, and HTMLReport.
# Write a function that accepts any report object.

class Report:
    def generate(self):
        pass


class PDFReport(Report):
    def generate(self):
        print("Generating PDF Report")


class ExcelReport(Report):
    def generate(self):
        print("Generating Excel Report")


class HTMLReport(Report):
    def generate(self):
        print("Generating HTML Report")


def generate_report(report):
    report.generate()


generate_report(PDFReport())
generate_report(ExcelReport())
generate_report(HTMLReport())
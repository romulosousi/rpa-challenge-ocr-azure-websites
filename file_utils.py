import os

def limpar_arquivos(csv_file, invoices_dir):
    if os.path.exists(csv_file):
        os.remove(csv_file)
        print(f"Arquivo {csv_file} removido.")

    if os.path.exists(invoices_dir):
        for filename in os.listdir(invoices_dir):
            file_path = os.path.join(invoices_dir, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
        print(f"Pasta invoice esvaziada. \n")

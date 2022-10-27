import csv


def save_account_data_in_csv(address: str):
    with open(f'res/wallets.csv', 'a+', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(
            [address])

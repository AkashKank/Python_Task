import xml.etree.ElementTree as ET
import pandas as pd

def process_xml(input_file):

    # Parse XML file
    tree = ET.parse(input_file)
    root = tree.getroot()

    # Extract relevant data for transactions with voucher type "Receipt"

    data = []
    for voucher in root.findall('.//VOUCHER'):
        voucher_type = voucher.find('.//VOUCHERTYPENAME').text
        if voucher_type == "Receipt":
            date = voucher.find('.//DATE').text
            voucher_number = voucher.find('.//VOUCHERNUMBER').text
            party_ledger = voucher.find('.//PARTYLEDGERNAME').text
            amount = voucher.find('.//ALLLEDGERENTRIES.LIST/AMOUNT').text
            transaction_type = voucher.find('.//ALLLEDGERENTRIES.LIST/BANKALLOCATIONS.LIST/TRANSACTIONTYPE').text
            payment_mode = voucher.find('.//ALLLEDGERENTRIES.LIST/BANKALLOCATIONS.LIST/PAYMENTMODE').text
            data.append([date, voucher_type, voucher_number, party_ledger, amount, transaction_type, payment_mode])

    # Create DataFrame
    df = pd.DataFrame(data, columns=['Date', 'Voucher Type', 'Voucher Number', 'Party Ledger', 'Amount', 'Transaction Type', 'Payment Mode'])
    return df


if __name__ == "__main__":
    input_file = "input.xml"
    output_file = "output.xlsx"

    df = process_xml(input_file)

    # Save Data Frame in Excel
    df.to_excel(output_file, index=False)

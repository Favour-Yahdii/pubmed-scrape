# how good is the model with extracting and summarising information from those primary studies to arrive at similar
# summaries to those in the original systematic reviews.

# starting with citation ckd
import pandas as pd
import os


class DoiExtract:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.df = pd.read_csv(self.csv_file)
        self.doi = self.df['DOI']

    def extract_doi(self):
        """
        args: None
        returns a list of dois
        """
        doi_list = []
        for i in self.doi:
            doi_list.append(i)
        return doi_list

    def extract_to_txt(self):
        """
        args: None
        returns a text file with the extracted dois
        """
        # check if text file with csv name exists
        base_name = os.path.splitext(self.csv_file)[0]
        txt_file = base_name + '.txt'
        if os.path.exists(txt_file):
            print('File already exists')
        else:
            with open(txt_file, 'w') as f:
                for i in self.doi:
                    f.write(str(i) + '\n')
            print('File created')

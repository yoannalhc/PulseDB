# You need to install the package mat73 because PulseDB uses MAT file version 7.3 to store large volume data
from mat73 import loadmat
import numpy as np


def Build_Dataset(Path, FieldName='Subset'):
    Data = loadmat(Path)
    for key, value in Data.items():
        print(key)
        for key2, value2 in value.items():
            print(key2)

    Signals = Data[FieldName]['Signals'][0]
    print("signals", Signals)

    # # Access 10-s segments of ECG, PPG and ABP signals
    # Signals = Data[FieldName]['Signals']
    # # Access SBP labels of each 10-s segment
    # SBPLabels = Data[FieldName]['SBP']
    # # Access Age of the subject corresponding to each of the 10-s segment
    # Age = Data[FieldName]['Age']
    # # Access Gender of the subject corresponding to each of the 10-s segment
    # Gender = np.array(Data[FieldName]['Gender']).squeeze()
    # # Convert Gender to numerical 0-1 labels
    # Gender = (Gender == 'M').astype(float)
    # # Access Height and Weight of the subject corresponding to each of the 10-s segment
    # # If the subject is from the MIMIC-III matched subset, height and weight will be NaN
    # # since they were only recorded in VitalDB
    # Height = Data[FieldName]['Height']
    # Weight = Data[FieldName]['Weight']
    # # Concatenate the demographic information as one matrix
    # Demographics = np.stack((Age, Gender, Height, Weight), axis=1)
    # return Signals, SBPLabels, Demographics

if __name__ == "__main__":
    #Build_Dataset('./data/VitalDB_Train_Subset.mat')
    Build_Dataset('./Supplementary_Subset_Files/VitalDB_AAMI_Test_Subset.mat')

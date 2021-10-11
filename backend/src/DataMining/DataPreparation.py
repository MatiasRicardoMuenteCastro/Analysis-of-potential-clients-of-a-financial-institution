import numpy as np
import pandas as pd

#Função para verificar se alguma string que contém um número float é um número inteiro
def VerifyIsAnInteger(str):
    str = float(str)
    VerifyInt = str % 1
    if VerifyInt > 0:
        return False
    else:
        return True

#Função para verificar se alguma string contém um número float
def FloatInSTR(str):
    try:
        str = float(str)
        return True
    except:
        return False

#Função para verificar se alguma string contém um número inteiro
def IntInString(str):
    try:
        str = int(str)
        return True
    except:
        return False

#Função que procura tipos de váriaveis divergentes com o tipo principal da coluna
def WrongTypeColumnsFound(Bank_Data):
    StrColumns = []
    IntColumns = []
    FloatColumns = []
    UndefinedColumns = []
    RemoveLines = []


    for columns in list(Bank_Data.columns):
        countString = 0
        countInt = 0
        countFloat = 0

        for item in Bank_Data[columns]:
            if type(item) == str:
                if FloatInSTR(item) == True:
                    if VerifyIsAnInteger(item) == True:
                        countInt = countInt+1
                    else:
                        countFloat = countFloat + 1
                else:
                    countString = countString+1
            elif type(item) == int:
                countInt = countInt+1
            elif type(item) == float:
                countFloat = countFloat+1

        if countString > countFloat and countString > countInt:
            StrColumns.append(columns)
        elif countFloat > countString and countFloat > countInt:
            FloatColumns.append(columns)
        elif countInt > countFloat and countInt > countString:
            IntColumns.append(columns)
        elif countString == countFloat or countString == countInt or countFloat == countInt:
            UndefinedColumns.append(columns)

    if len(IntColumns) > 0:
        for columns in IntColumns:
            LinePosition = 0
            for item in Bank_Data[columns]:
                if type(item) != int:
                    RemoveLines.append(LinePosition)
                LinePosition = LinePosition + 1

    if len(StrColumns) > 0:
        for columns in StrColumns:
            LinePosition = 0
            for item in Bank_Data[columns]:
                if type(item) != str or FloatInSTR(item) == True or IntInString(item) == True:
                    RemoveLines.append(LinePosition)
                LinePosition = LinePosition + 1

    if len(FloatColumns) > 0:
        for columns in FloatColumns:
            LinePosition = 0
            for item in Bank_Data[columns]:
                if type(item) != float:
                    RemoveLines.append(LinePosition)
                LinePosition = LinePosition + 1

    Bank_Data = Bank_Data.drop(Bank_Data.index[RemoveLines]).reset_index(drop=True)
    return Bank_Data

#Função para encontrar valores outliers por meio da formula z_score
def find_outlier(column):
    OutlierCount = 0
    outliers = []

    cut_sd = 2
    mean = np.mean(column)
    standard_deviation = np.std(column)

    for i in column:
        z_score = (i - mean) / standard_deviation
        if np.abs(z_score) >= cut_sd:
            outliers.append(i)
            OutlierCount = OutlierCount+1

    return OutlierCount,outliers

#Função para encontrar valores outliers por meio do intervalo interquertil
def find_quantile_outlier(column):
    outliers = []
    count = 0
    q1 = np.quantile(column,.25)
    q3 = np.quantile(column,.75)
    iq = q3-q1
    bottom = q1 - (1.5*iq)
    top = q3 + (1.5*iq)

    for i in column:
        if i > top or i < bottom:
            count = count+1
            outliers.append(i)

    return count,outliers

def Data_Preparation(Bank_Data):
    #Função para retirar todos os tipos divergentes do da coluna
    Bank_Data = WrongTypeColumnsFound(Bank_Data)

    #Transforma toda a tabela em lowercase
    for columns in list(Bank_Data.columns):
        try:
            Bank_Data[columns] = Bank_Data[columns].str.lower()
        except:
            Bank_Data[columns]

    #Substitui o dado "Desconhecido" pelo dado Nulo do numpy para sua remoção, depois dessa substituição eles passam a ser de "Desconhecidos" para Nulos.
    #Se for necessário poderemos substituir a string 'unknown' por uma lista de palavras a serem substituidas por NAN
    Bank_Data = Bank_Data.replace('unknown',np.nan)
    Bank_Data['poutcome'] = Bank_Data['poutcome'].replace(np.nan,'unknown')
    Bank_Data = Bank_Data.dropna().reset_index(drop = True)

    #Verifica se existem linhas duplicadas no código e se elas existirem sua remoção é feita
    if (Bank_Data.duplicated().sum() > 0):
        Bank_Data = Bank_Data.drop_duplicates()

    #Cria agrupamentos nas colunas AGE, BALANCE, DURATION e CAMPAIGN
    Bank_Data['age_agroupment'] = pd.cut(x = Bank_Data['age'], bins = [18,24,30,36,42,48,54,60,66,72,78,84,90,96], right= False)
    Bank_Data['balance_agroupment'] = pd.cut(x = Bank_Data['balance'], bins = [-30000,-20000,-15000,-10000,-8000,-6000,-4000,-2000,-1000,-500,0,500,1000,2000,4000,6000,8000,10000,15000,20000,30000,40000,50000,60000,70000,80000,90000,100000,105000])
    Bank_Data['duration_agroupment'] = pd.cut(x = Bank_Data['duration'], bins = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000,1200,1400,1600,1800,2000,2400,2600,2800,3000,3200,3400,3500,4000,4500,5000],right= False)
    Bank_Data['campaign_agroupment'] = pd.cut(x = Bank_Data['campaign'],bins = [0,2,4,6,8,9,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50])
    Bank_Data['previous_agroupment'] = pd.cut(x = Bank_Data['previous'],bins = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80], right = False)

    #Loop de repetição para percorrer todas as tabelas em busca dos dados outliers para sua remoção
    for columns in list(Bank_Data.columns):
        New_List_Columns = []
        if(columns.lower() == 'balance' or columns.lower() == 'duration' or columns.lower() == 'campaign' or columns.lower() == 'pdays' or columns.lower() == 'previous'):
            New_List_Columns.append(columns)
        for values in New_List_Columns:
            outliers = find_outlier(Bank_Data[values])
            outliers_amount = outliers[0]
            outliers = outliers[1]
            if outliers_amount > 0:
                Bank_Data[values] = Bank_Data[values].replace(outliers, np.nan)

    Bank_Data = Bank_Data.dropna().reset_index(drop = True)

    return Bank_Data
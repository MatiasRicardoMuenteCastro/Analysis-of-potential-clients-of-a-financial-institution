import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Plota o gráfico dos saldos de cada faixa etária
def AgeWithBalance(Bank_Data):
    Bank_Data = Bank_Data.sort_values('age')
    plt.figure(figsize = (13,8))
    plt.style.use("ggplot")
    plt.title("Faixa de saldo por ano em relação a idade dos clientes em euros")
    sns.stripplot(x = 'age_agroupment', y = 'balance',data = Bank_Data)
    plt.xlabel("Idade dos clientes")
    plt.ylabel("Faixa de saldo")
    plt.show(block = True)

#Plota o gráfico da duração de chamada por idade
def AgeWithDuration(Bank_Data):
    Bank_Data = Bank_Data.sort_values('duration',ascending = False)
    plt.figure(figsize = (13,8))
    plt.style.use("ggplot")
    plt.title("Tempo médio de duração de uma chamada de marketing por faixa etária (Segundos)")
    sns.lineplot(x = 'age', y = 'duration', data = Bank_Data,alpha = 0.75)
    plt.xlabel('Idade')
    plt.ylabel('Tempo médio de duração')
    plt.show(block = True)

def ClientsQuantityAge(Bank_Data):
    AgesCount = pd.DataFrame(pd.value_counts(Bank_Data['age']))
    AgesDF = pd.DataFrame({"age": AgesCount.index,"quantity" : AgesCount['age']})
    AgesDF = AgesDF.reset_index(drop = True)

    figure = plt.figure(figsize=(18,6))
    figure.set_size_inches(30, 6)
    plt.style.use("ggplot")
    plt.title("Faixa etária dos clientes do banco")
    sns.barplot(x = 'age',y = 'quantity', data = AgesDF, alpha = 0.75)
    plt.ylabel("Número de clientes")
    plt.xlabel("Idades")
    plt.show(block = True)

def AgeMarital(Bank_Data):
    plt.figure(figsize = (13,7))
    plt.style.use("ggplot")
    plt.title("Idade dos clientes que estão casadas solteiras ou divorciadas")
    sns.boxplot(x = 'marital', y = 'age', data = Bank_Data)
    plt.xlabel("Estado civil")
    plt.ylabel("Idade")
    plt.show(block = True)

def JobsQuanity(Bank_Data):
    JobValues = pd.value_counts(Bank_Data["job"])
    JobDF = pd.DataFrame({"quantity": JobValues})
    JobDF = JobDF.reset_index()

    plt.figure(figsize=(15,6))
    plt.style.use("ggplot")
    plt.title("Quantidade de pessoas que estão em determinados empregos")
    sns.barplot(x = 'index', y = 'quantity', data = JobDF,alpha = 0.75)
    plt.xlabel("Empregos")
    plt.ylabel("Quantidade de clientes")
    plt.show(block = True)

def BalanceWithJob(Bank_Data):
    plt.figure(figsize=(15, 6))
    plt.style.use("ggplot")
    plt.title("Saldo médio por ano de cada profissão em euros")
    sns.stripplot(x = 'job', y = 'balance',data = Bank_Data)
    plt.xlabel("Empregos")
    plt.ylabel("Saldo médio")
    plt.show(block = True)

def AgeWithLoan(Bank_Data):
    Bank_Data = Bank_Data.sort_values('age')
    tempArray = []
    for line in list(range(Bank_Data['age_agroupment'].count())):
        tempArray.append(Bank_Data.iloc[line]['age_agroupment']+" "+Bank_Data.iloc[line]['loan'])

    AgeLoanDF = pd.DataFrame({"Age     Loan": tempArray})

    plt.figure(figsize = (15,6))
    plt.title("O volume das idades que contem algum emprestimo")
    plt.style.use("ggplot")
    sns.countplot(y = 'Age     Loan',data = AgeLoanDF)
    plt.xlabel("Quantidades de clientes")
    plt.ylabel("Grupos das idades dos clientes")
    plt.show(block = True)

def AgeWithHousing(Bank_Data):
    Bank_Data = Bank_Data.sort_values('age')
    tempArray = []
    for line in list(range(Bank_Data['age_agroupment'].count())):
        tempArray.append(Bank_Data.iloc[line]['age_agroupment'] + " " + Bank_Data.iloc[line]['housing'])

    AgeHousingDF = pd.DataFrame({"Age Housing": tempArray})

    plt.figure(figsize=(15, 6))
    plt.style.use("ggplot")
    plt.title("O volume das idades que contem o financiamento de uma casa")
    sns.countplot(y = 'Age Housing',data = AgeHousingDF)
    plt.xlabel("Quantidade de clientes")
    plt.ylabel("Grupos das idades dos clientes")
    print(AgeHousingDF.value_counts())
    plt.show(block=True)

def AgeWithDefault(Bank_Data):
    Bank_Data = Bank_Data.sort_values('age')
    tempArray = []
    for line in list(range(Bank_Data['age_agroupment'].count())):
        tempArray.append(Bank_Data.iloc[line]['age_agroupment'] + " " + Bank_Data.iloc[line]['default'])

    AgeDefaultDF = pd.DataFrame({"Age Default": tempArray})

    plt.figure(figsize=(15, 6))
    plt.style.use("ggplot")
    plt.title("O volume das idades que estão com o nome sujo")
    sns.countplot(y = 'Age Default',data = AgeDefaultDF)
    plt.xlabel("Quantidade de clientes")
    plt.ylabel("Grupos das idades dos clientes")
    print(AgeDefaultDF.value_counts())
    plt.show(block=True)

def ContactWithDuration(Bank_Data):
    plt.figure(figsize = (15,6))
    plt.style.use("ggplot")
    plt.title("Tipo de contato que os clientes mais utilizam")
    sns.stripplot(x = 'contact', y = 'duration', data = Bank_Data)
    plt.xlabel('Tipo de contato')
    plt.ylabel('Duração do contato')
    plt.show(block = True)

def ContactWithAge(Bank_Data):
    Bank_Data = Bank_Data.sort_values('age')
    tempArray = []
    for line in list(range(Bank_Data['age_agroupment'].count())):
        tempArray.append(Bank_Data.iloc[line]['age_agroupment'] + " " + Bank_Data.iloc[line]['contact'])

    AgeContactDF = pd.DataFrame({"Age Contact": tempArray})

    plt.figure(figsize=(15, 6))
    plt.style.use("ggplot")
    plt.title("Idades que mais utilizam determinados tipos de contatos")
    sns.countplot(y='Age Contact', data=AgeContactDF)
    plt.ylabel('Groupo Etário / Tipo de contato')
    plt.show(block = True)

def StatusCampaigns(Bank_Data):
    TempArray = []
    line = 0
    for item in Bank_Data['poutcome']:
        line = line+1
        if item != 'unknown' and item != 'other':
            TempArray.append(item)

    StatusDF = pd.DataFrame({'Status':TempArray})

    plt.figure(figsize=(10, 6))
    plt.style.use("ggplot")
    plt.title("Status das campanhas de marketing até agora feitas")
    sns.countplot(x = 'Status',data = StatusDF)
    plt.xlabel('Status da campanha')
    plt.ylabel('Quantidades de falha ou sucesso')
    plt.show(block=True)

file_path = "./Dataset/Bank_Data.xlsx"
Bank_Data = pd.read_excel(file_path)


#AgeWithBalance(Bank_Data)
#AgeWithDuration(Bank_Data)
#ClientsQuantityAge(Bank_Data)
#AgeMarital(Bank_Data)
#JobsQuanity(Bank_Data)
#BalanceWithJob(Bank_Data)
#AgeWithLoan(Bank_Data)
#AgeWithHousing(Bank_Data)
#AgeWithDefault(Bank_Data)
#ContactWithDuration(Bank_Data)
#ContactWithAge(Bank_Data)
#StatusCampaigns(Bank_Data)
#Fazer o value.counts de cada dataframe possivel para enviar ao front-end
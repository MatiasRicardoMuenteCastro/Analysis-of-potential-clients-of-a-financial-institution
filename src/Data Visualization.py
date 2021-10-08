import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Plota o gráfico dos saldos de cada faixa etária
def AgeWithBalance(Bank_Data):
    custom_style = {'axes.labelcolor': 'black',
                    'xtick.color': 'black',
                    'ytick.color': '#3b157e'}
    new_style = {'grid': False}

    Bank_Data = Bank_Data.sort_values('age')
    plt.figure(figsize = (13,8))
    plt.style.use("ggplot")
    plt.rc('axes', **new_style)
    sns.set_style(rc=custom_style)
    plt.title("Faixa de saldo por ano em relação à idade dos clientes em euros")
    sns.stripplot(x = 'age_agroupment', y = 'balance',data = Bank_Data, palette = "flare", alpha = 0.75)
    plt.xlabel("Idade dos clientes")
    plt.ylabel("Faixa de saldo")
    plt.show(block = True)

#Plota o gráfico da duração de chamada por idade
def AgeWithDuration(Bank_Data):
    custom_style = {'axes.labelcolor': 'black',
                    'xtick.color': 'black',
                    'ytick.color': '#FA2B5D'}
    new_style = {'grid': False}

    Bank_Data = Bank_Data.sort_values('duration',ascending = False)
    plt.figure(figsize = (13,8))
    plt.style.use("ggplot")
    plt.rc('axes', **new_style)
    sns.set_style(rc=custom_style)
    plt.title("Tempo médio de duração de uma ligação de marketing por faixa etária (Segundos)")
    sns.lineplot(x = 'age', y = 'duration', data = Bank_Data,alpha = 0.75)
    plt.xlabel('Idade')
    plt.ylabel('Tempo médio de duração')
    plt.show(block = True)

def ClientsQuantityAge(Bank_Data):
    custom_style = {'axes.labelcolor': 'black',
                    'xtick.color': '#3b157e',
                    'ytick.color': '#3b157e'}
    new_style = {'grid': False}

    AgesCount = pd.DataFrame(pd.value_counts(Bank_Data['age']))
    AgesDF = pd.DataFrame({"age": AgesCount.index,"quantity" : AgesCount['age']})
    AgesDF = AgesDF.reset_index(drop = True)

    figure = plt.figure(figsize=(18,6))
    figure.set_size_inches(30, 6)
    plt.style.use("ggplot")
    plt.rc('axes', **new_style)
    sns.set_style(rc=custom_style)
    plt.title("Faixa etária dos clientes do banco")
    sns.barplot(x = 'age',y = 'quantity', data = AgesDF, palette = "magma", alpha = 0.75)
    plt.ylabel("Número de clientes")
    plt.xlabel("Idades")
    plt.show(block = True)

def AgeMarital(Bank_Data):
    custom_style = {'axes.labelcolor': 'black',
                    'xtick.color': 'black',
                    'ytick.color': '#3b157e'}
    new_style = {'grid': False}

    plt.figure(figsize = (13,7))
    plt.style.use("ggplot")
    plt.rc('axes', **new_style)
    sns.set_style(rc=custom_style)
    plt.title("Estado civil dos clientes da instituição financeira")
    sns.stripplot(x = 'marital', y = 'age', data = Bank_Data,alpha = 0.75,palette = "flare")
    plt.xlabel("Estado civil")
    plt.ylabel("Idade")
    plt.show(block = True)

def JobsQuanity(Bank_Data):
    custom_style = {'axes.labelcolor': 'black',
                    'xtick.color': '#3b157e',
                    'ytick.color': '#3b157e'}
    new_style = {'grid': False}

    JobValues = pd.value_counts(Bank_Data["job"])
    JobDF = pd.DataFrame({"quantity": JobValues})
    JobDF = JobDF.reset_index()

    print(JobDF.sort_values('quantity',ascending= False))

    plt.figure(figsize=(15,6))
    plt.style.use("ggplot")
    plt.rc('axes', **new_style)
    sns.set_style(rc=custom_style)
    plt.title("Quantidade de pessoas que estão em determinados empregos")
    sns.barplot(x = 'index', y = 'quantity', data = JobDF,alpha = 0.75, palette = "magma")
    plt.xlabel("Empregos")
    plt.ylabel("Quantidade de clientes")
    plt.show(block = True)

def BalanceWithJob(Bank_Data):
    custom_style = {'axes.labelcolor': 'black',
                    'xtick.color': 'black',
                    'ytick.color': '#3b157e'}
    new_style = {'grid': False}

    plt.figure(figsize=(15, 6))
    plt.style.use("ggplot")
    plt.rc('axes', **new_style)
    sns.set_style(rc=custom_style)
    plt.title("Saldo médio por ano de cada profissão em euros")
    sns.stripplot(x = 'job', y = 'balance',data = Bank_Data, alpha = 0.75, palette = "flare")
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
    plt.title("O volume das idades que têm algum emprestimo")
    plt.style.use("ggplot")
    sns.countplot(y = 'Age     Loan',data = AgeLoanDF, palette = "magma", alpha = 0.75)
    plt.xlabel("Quantidades de clientes")
    plt.ylabel("Grupos das idades dos clientes")
    print(AgeLoanDF.value_counts())
    plt.show(block = True)

def AgeWithHousing(Bank_Data):
    custom_style = {'axes.labelcolor': 'black',
                    'xtick.color': '#3b157e',
                    'ytick.color': '#3b157e'}
    new_style = {'grid': False}
    Bank_Data = Bank_Data.sort_values('age')
    tempArray = []
    for line in list(range(Bank_Data['age_agroupment'].count())):
        tempArray.append(Bank_Data.iloc[line]['age_agroupment'] + " " + Bank_Data.iloc[line]['housing'])

    AgeHousingDF = pd.DataFrame({"Age Housing": tempArray})

    plt.figure(figsize=(15, 6))
    plt.style.use("ggplot")
    plt.rc('axes', **new_style)
    sns.set_style(rc=custom_style)
    plt.title("O volume das idades que têm financiamento de uma casa")
    sns.countplot(y = 'Age Housing',data = AgeHousingDF, palette = "magma", alpha = 0.75)
    plt.xlabel("Quantidade de clientes")
    plt.ylabel("Grupos das idades dos clientes")
    print(AgeHousingDF.value_counts())
    plt.show(block=True)

def AgeWithDefault(Bank_Data):
    custom_style = {'axes.labelcolor': 'black',
                    'xtick.color': '#3b157e',
                    'ytick.color': '#3b157e'}
    new_style = {'grid': False}
    Bank_Data = Bank_Data.sort_values('age')
    tempArray = []
    for line in list(range(Bank_Data['age_agroupment'].count())):
        tempArray.append(Bank_Data.iloc[line]['age_agroupment'] + " " + Bank_Data.iloc[line]['default'])

    AgeDefaultDF = pd.DataFrame({"Age Default": tempArray})

    plt.figure(figsize=(15, 6))
    plt.style.use("ggplot")
    plt.rc('axes', **new_style)
    sns.set_style(rc=custom_style)
    plt.title("O volume das idades que estão com o nome sujo")
    sns.countplot(y = 'Age Default',data = AgeDefaultDF, alpha = 0.75, palette = "magma")
    plt.xlabel("Quantidade de clientes")
    plt.ylabel("Grupos das idades dos clientes")
    print(AgeDefaultDF.value_counts())
    plt.show(block=True)

def ContactWithDuration(Bank_Data):
    custom_style = {'axes.labelcolor': 'black',
                    'xtick.color': 'black',
                    'ytick.color': '#3b157e'}
    new_style = {'grid': False}

    plt.figure(figsize = (15,6))
    plt.style.use("ggplot")
    plt.rc('axes', **new_style)
    sns.set_style(rc=custom_style)
    plt.title("Meio de contato que os clientes ficam conversando por mais tempo")
    sns.stripplot(x = 'contact', y = 'duration', data = Bank_Data, alpha = 0.75, palette = "flare")
    plt.xlabel('Tipo de contato')
    plt.ylabel('Duração do contato')
    plt.show(block = True)

def ContactWithAge(Bank_Data):
    custom_style = {'axes.labelcolor': 'black',
                    'xtick.color': '#3b157e',
                    'ytick.color': '#3b157e'}
    new_style = {'grid': False}
    Bank_Data = Bank_Data.sort_values('age')
    tempArray = []
    for line in list(range(Bank_Data['age_agroupment'].count())):
        tempArray.append(Bank_Data.iloc[line]['age_agroupment'] + " " + Bank_Data.iloc[line]['contact'])

    AgeContactDF = pd.DataFrame({"Age Contact": tempArray})

    plt.figure(figsize=(15, 6))
    plt.style.use("ggplot")
    plt.rc('axes', **new_style)
    sns.set_style(rc=custom_style)
    plt.title("Idades que mais utilizam determinados meios de contatos")
    sns.countplot(y='Age Contact', data=AgeContactDF, palette = "magma", alpha = 0.75)
    plt.ylabel('Groupo Etário / Tipo de contato')
    plt.xlabel('Quantidade de pessoas')
    plt.show(block = True)

def StatusCampaigns(Bank_Data):
    custom_style = {'axes.labelcolor': 'black',
                    'xtick.color': 'black',
                    'ytick.color': '#3b157e'}
    new_style = {'grid': False}
    TempArray = []
    line = 0
    for item in Bank_Data['poutcome']:
        line = line+1
        if item != 'unknown' and item != 'other':
            TempArray.append(item)

    StatusDF = pd.DataFrame({'Status':TempArray})

    plt.figure(figsize=(10, 6))
    plt.style.use("ggplot")
    plt.rc('axes', **new_style)
    sns.set_style(rc=custom_style)
    plt.title("Status das campanhas de marketing até agora feitas")
    sns.countplot(x = 'Status',data = StatusDF, alpha = 0.75, palette = "magma")
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
AgeWithLoan(Bank_Data)
#AgeWithHousing(Bank_Data)
#AgeWithDefault(Bank_Data)
#ContactWithDuration(Bank_Data)
#ContactWithAge(Bank_Data)
#StatusCampaigns(Bank_Data)
#Fazer o value.counts de cada dataframe possivel para enviar ao front-end
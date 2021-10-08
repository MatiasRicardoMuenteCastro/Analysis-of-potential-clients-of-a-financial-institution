import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def OrganizeAscending(Bank_Data,job):
    line = 0
    balance = []
    Bank_Data = Bank_Data.sort_values('balance')
    for item in Bank_Data['job']:
        if item.lower() == job:
            balance.append(Bank_Data.iloc[line]['balance_agroupment'])
        line = line + 1

    BalanceSeries = pd.Series(pd.value_counts(balance))
    BalanceDF = pd.DataFrame({"balance_agroupment": BalanceSeries.index, "quantity": BalanceSeries})
    BalanceDF = BalanceDF.reset_index(drop=True)

    group = []
    for item in BalanceDF['balance_agroupment']:
        split1 = item.split("(")
        for i in split1:
            split2 = i.split("]")
            for split2item in split2:
                split3 = split2item.split(",")
                for split3item in split3:
                    if split3item != "":
                        group.append(split3)

    groupSeries = pd.Series(group)
    groupSeries = groupSeries.drop_duplicates()
    groupSeries = groupSeries.reset_index(drop=True)
    num1 = []

    for x in groupSeries:
        for j in range(0, len(x), 2):
            num1.append(int(x[j]))

    BalanceDF = pd.DataFrame({"organize": num1, "balance_agroupment": BalanceSeries.index, "quantity": BalanceSeries})
    BalanceDF = BalanceDF.reset_index(drop=True)
    BalanceDF = BalanceDF.sort_values("organize").reset_index(drop=True)

    return BalanceDF

def BalanceWithBlueCollar(Bank_Data):
    custom_style = {'axes.labelcolor': 'black',
                    'xtick.color': '#3b157e',
                    'ytick.color': '#3b157e'}
    new_style = {'grid': False}
    BlueCollarDF = OrganizeAscending(Bank_Data,'blue-collar')
    plt.figure(figsize=(15, 6))
    plt.style.use("ggplot")
    plt.rc('axes', **new_style)
    sns.set_style(rc=custom_style)
    plt.title("Saldo dos clientes que são trabalhadores de colarinho azul (euros)")
    sns.barplot(x='balance_agroupment', y='quantity', data=BlueCollarDF, alpha = 0.75, palette = "magma")
    plt.xlabel("Faixa de saldo")
    plt.ylabel("Quantidade de clientes")
    BlueCollarCount = BlueCollarDF.value_counts()
    plt.show(block=True)

def BalanceWithRetired(Bank_Data):
    custom_style = {'axes.labelcolor': 'black',
                    'xtick.color': '#3b157e',
                    'ytick.color': '#3b157e'}
    new_style = {'grid': False}
    RetiredDF = OrganizeAscending(Bank_Data, 'retired')
    plt.figure(figsize=(17, 6))
    plt.style.use("ggplot")
    plt.rc('axes', **new_style)
    sns.set_style(rc=custom_style)
    plt.title("Saldo dos clientes que estão aposentados (euros)")
    sns.barplot(x='balance_agroupment', y='quantity', data=RetiredDF, alpha = 0.75, palette = "magma")
    plt.xlabel("Faixa de saldo")
    plt.ylabel("Quantidade de clientes")
    RetiredCount = RetiredDF.value_counts()
    print(RetiredCount)
    plt.show(block = True)

def BalanceWithManagement(Bank_Data):
    custom_style = {'axes.labelcolor': 'black',
                    'xtick.color': '#3b157e',
                    'ytick.color': '#3b157e'}
    new_style = {'grid': False}
    ManagementDF = OrganizeAscending(Bank_Data, 'management')
    group = []
    for item in ManagementDF['balance_agroupment']:
        split1 = item.split("(")
        for i in split1:
            split2 = i.split("]")
            for split2item in split2:
                split3 = split2item.split(",")
                for split3item in split3:
                    if split3item != "":
                        group.append(split3)
    groupString = []
    for i in group:
        groupString.append(''.join(i))

    groupSeries = (pd.Series(groupString))
    groupSeries = groupSeries.drop_duplicates().reset_index(drop = True)
    ManagementDF['balance_agroupment'] = groupSeries
    plt.figure(figsize=(20, 6))
    plt.style.use("ggplot")
    plt.rc('axes', **new_style)
    sns.set_style(rc=custom_style)
    plt.title("Saldo dos clientes que são gerentes (euros)")
    sns.barplot(x='balance_agroupment', y='quantity', data=ManagementDF, alpha = 0.75, palette = "magma")
    plt.xlabel("Faixa de saldo")
    plt.ylabel("Quantidade de clientes")
    ManagmentCount = ManagementDF.value_counts()
    print(ManagmentCount)
    plt.show(block = True)


def BalanceWithTechnician(Bank_Data):
    custom_style = {'axes.labelcolor': 'black',
                    'xtick.color': '#3b157e',
                    'ytick.color': '#3b157e'}
    new_style = {'grid': False}
    technician = OrganizeAscending(Bank_Data, 'technician')
    plt.figure(figsize=(18, 6))
    plt.style.use("ggplot")
    plt.rc('axes', **new_style)
    sns.set_style(rc=custom_style)
    plt.title("Saldo dos clientes que são tecnicos (euros)")
    sns.barplot(x='balance_agroupment', y='quantity', data=technician, alpha = 0.75, palette = "magma")
    plt.xlabel("Faixa de saldo")
    plt.ylabel("Quantidade de clientes")
    TechnicianCount = technician.value_counts()
    print(TechnicianCount)
    plt.show(block=True)

def BalanceWithAdmin(Bank_Data):
    custom_style = {'axes.labelcolor': 'black',
                    'xtick.color': '#3b157e',
                    'ytick.color': '#3b157e'}
    new_style = {'grid': False}
    admins = OrganizeAscending(Bank_Data, 'admin.')
    plt.figure(figsize=(18, 6))
    plt.style.use("ggplot")
    plt.rc('axes', **new_style)
    sns.set_style(rc=custom_style)
    plt.title("Saldo dos clientes que são administradores (euros)")
    sns.barplot(x='balance_agroupment', y='quantity', data=admins,alpha = 0.75,palette = "magma")
    plt.xlabel("Faixa de saldo")
    plt.ylabel("Quantidade de clientes")
    AdminsCount = admins.value_counts()
    print(AdminsCount)
    plt.show(block=True)

def BalanceWithServices(Bank_Data):
    custom_style = {'axes.labelcolor': 'black',
                    'xtick.color': '#3b157e',
                    'ytick.color': '#3b157e'}
    new_style = {'grid': False}
    services = OrganizeAscending(Bank_Data, 'services')
    plt.figure(figsize=(18, 6))
    plt.style.use("ggplot")
    plt.rc('axes', **new_style)
    sns.set_style(rc=custom_style)
    plt.title("Saldo dos clientes que trabalham na prestação de serviços (euros)")
    sns.barplot(x='balance_agroupment', y='quantity', data=services,alpha = 0.75, palette = "magma")
    plt.xlabel("Faixa de saldo")
    plt.ylabel("Quantidade de clientes")
    ServicesCount = services.value_counts()
    print(ServicesCount)
    plt.show(block=True)

file_path = "./Dataset/Bank_Data.xlsx"
Bank_Data = pd.read_excel(file_path)

#Grupo do saldo alto
#BalanceWithBlueCollar(Bank_Data)
#BalanceWithManagement(Bank_Data)
#BalanceWithTechnician(Bank_Data)
#Grupo do saldo alto/médio
#BalanceWithRetired(Bank_Data)
#BalanceWithAdmin(Bank_Data)
#BalanceWithServices(Bank_Data)

#Enviar o value counts de cada tabela, para dar uma noção maior sobre os valoresdo gráfico
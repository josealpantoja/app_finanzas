import matplotlib.pyplot as plt #es la libreria de grafias, y le ponemos el alias plt
import plotly.express as px

def generate_bar_chart(labels, values):
    fig, ax = plt.subplots() #primer es figura, y segunda coordinadas que comenzamos a graficar
    ax.bar(labels, values, color='red')
    ax.set_title('Gráfico de Barras del Balance')  # Añade un título al gráfico
    plt.show()

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots() 
    ax.pie(values, labels=labels) #debemos indicar el argumento labels  
    ax.axis('equal') #decirle que organice la frafica en el centro y que sea círculo
    plt.show()



def generate_bar_chart2(labels, values):
    fig = px.bar(x=labels, y=values, title='Gráfico de Barras del Balance', labels={'x': 'Categorías', 'y': 'Valores'})
    fig.show()



if __name__ == '__main__':
    
    labels = ['a', 'b', 'c'] #concepto  
    values = [10, 40, 800] #valres
    generate_bar_chart2(labels, values)
    generate_pie_chart(labels, values)
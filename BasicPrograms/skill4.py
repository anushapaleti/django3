import pandas as pd
import matplotlib.pyplot as plt
def read_csv_file(file_path):
    df = pd.read_csv(file_path)
    return df
def generate_graph(data_frame):
    x_values = data_frame['REGNUM']
    y_columns = data_frame.columns[1:]
    colors = ['b','g','r','c','m','y','k']
    for i, column in enumerate(y_columns):
        y_values = data_frame[column]
        plt.plot(x_values, y_values, marker='o', linestyle='-', label=column, color=colors[i])
        # plt.plot(X_values,Y_values,marker='o',linestyle ='-',label = column,color = colors)


    plt.xlabel('X-axis Label')
    plt.ylabel('Y-axis Label')
    plt.title('CSV Data Plot')
    plt.grid(True)
    plt.legend()
    plt.savefig("a1.png")
    plt.show()

if __name__ == "__main__":
    file_path = "TRY1.csv"
    data_frame = read_csv_file(file_path)
    generate_graph(data_frame)



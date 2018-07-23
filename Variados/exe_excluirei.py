from sklearn.datasets import load_iris
iris_dataset = load_iris()
print("Keys of iris_dataset: \n{}".format(iris_dataset.keys())) # keys aparentemente mostra os atributos
print(iris_dataset['DESCR'][:193]) #  O ATRIBUTO DESCR mostra uma descricao do dataset
print("Type of data: {}".format(type(iris_dataset['data'])))
print("Type of data: {}".format(iris_dataset['data'].shape))

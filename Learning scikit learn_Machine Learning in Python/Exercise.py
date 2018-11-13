#%%
import sklearn as sk
import numpy as np
import matplotlib.pyplot as plt

#%%
from sklearn.datasets import fetch_olivetti_faces
faces = fetch_olivetti_faces()
print(faces.keys())
#print(faces.images.shape)
print(np.max(faces.data))
print(np.min(faces.data))
print(np.mean(faces.data))

#%%
def print_faces(images, target, top_n):
    fig = plt.figure(figsize=(12, 12))
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)
    for i in range(top_n):
        p = fig.add_subplot(20, 20, i+1, xticks=[], yticks=[])
        p.imshow(images[i], cmap = plt.cm.bone) 
        p.text(0, 14, str(target[i]))
        p.text(0, 60, str(i))

# print(faces.images)
print_faces(faces.images, faces.target, 20)


# importing the Support Vector Classifier class from Support Vector Machine
from sklearn.svm import SVC
classifier_svc_1 = SVC(kernel='linear')

# Splitting the dataset into training and test sets
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(faces.data, faces.target, test_size = 0.25, random_state = 0)

# A function which evaluates the K-fold cross-validation
from sklearn.cross_validation import cross_val_score, KFold
from scipy.stats import sem

#%%
def evaluate_cross_validation(clf, X, y, K):
    # a k-fold cross validation iterator
    class_valid = KFold(len(y), K, shuffle=True, random_state=0)
    # 
    scores = cross_val_score(clf, X, y, cv = class_valid)
    print(scores)
    print(("Mean score: {0:.3f} (+/-{1:.3f})").format(np.mean(scores), sem(scores)))

#%%
evaluate_cross_validation(classifier_svc_1, X_train, y_train, 5)

# defining a function to perform training on training set and evaluate
# the performance on testing set
from sklearn import metrics

def train_and_evaluate(generic_classifier, X_train, X_test, y_train, y_test):

    generic_classifier.fit(X_train, y_train)

    print("Accuracy on training set:")
    print(generic_classifier.score(X_train, y_train))
    print("Accuracy on testing set:")
    print(generic_classifier.score(X_test, y_test))

    y_pred = generic_classifier.predict(X_test)

    print("Classification Report:")
    print(metrics.classification_report(y_test, y_pred))
    print("Confusion Matrix:")
    print(metrics.confusion_matrix(y_test, y_pred))

#%%
train_and_evaluate(classifier_svc_1, X_train, X_test, y_train, y_test)
import statsmodels.api as sm
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df = pd.read_csv('C:/Users/apers/Downloads/GloblocData/Generalization/discr_TestPhase_means_PerSub.csv')

inputs = df['distances']

labels = df['means']

inputs_train, inputs_test, labels_train, labels_test = train_test_split(inputs, labels, test_size=0.3, random_state=42)


log_reg = sm.Logit(labels, inputs).fit()

print(log_reg.summary())
exit()
yhat = log_reg.predict(inputs_test)
prediction = list(map(round, yhat))

print('Actual values', list(labels_test.values))
print('Predictions :', prediction)

print('Test accuracy = ', accuracy_score(labels_test, prediction))

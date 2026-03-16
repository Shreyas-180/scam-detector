import pickle
with open('bayes_model.pkl', 'rb') as f:
    bayes_model = pickle.load(f)
    
def checker(new_message, bayes_model):
    pred = bayes_model.predict(new_message)
    score = bayes_model.predict_proba(new_message)
    if(pred[0] == 1):
        pred = 'spam!'
    else:
        pred = 'not spam!'
    s1 = float(score[0][0])
    s2 = float(score[0][1])
    s = -1
    if(s1>s2):
        s = s1
    else:
        s = s2
    print(pred,s)

checker(['Acme Bank: Suspicious activity detected. Secure your account by verifying your identity at'],bayes_model)
import pickle
# with open('bayes_model.pkl','rb') as f:
#     bayes_model = pickle.load(f)
# new_email =["Congratulations! You've won a $1,000 Nyka gift card. Click here to claim."]
# pred = bayes_model.predict(new_email)
# score = bayes_model.predict_proba(new_email)
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
    return [pred,s]
# print("The Message is ",pred,"with a confidence of ",s*100)
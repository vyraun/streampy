## Coefs:
{
  "experimentID" : 1134123,
  "update":{
    "theta":{"Na":0, "Nb":0, "Sa":0, "Sb":0},
    "rules":{
      "Na" : "increment[action==A]",
      "Nb" : "increment[action==B]",
      "Sa" : "increment[action==A&reward==1]",
      "Sb" : "increment[action==B&reward==1]"
    }
    
  },
  "advice":"rand(A,B)"
}
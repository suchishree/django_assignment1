from django.shortcuts import render
def show(request):
    student_info = {"data":[{"idno":101,"name":"ravi","marks":[55,79,98,45,30,16]},
                             {"idno":102,"name":"kumar","marks":[98,65,78,2,12,90]},
                             {"idno":103,"name":"mohan","marks":[59,67,"A",90,21,65]},
                             {"idno":104,"name":"krishna","marks":[78,65,44,77,88,11]},
                             {"idno":105,"name":"hari","marks":[80,76,"A",99,100,88]},
                             {"idno":106,"name":"radha","marks":[44,57,68,61,23,60]}
                            ]
                            }
    return render(request,"demo.html",student_info)

from django.shortcuts import redirect, render,HttpResponse
import operator
candidates = dict()
ids = []
# Create your views here.
def home(request):
    all_values = candidates.values()
    print(all_values)
    return render(request,"home.html")

def add_candidates(request,alert=''):
    if request.method == "POST":
        candidate = request.POST.get("candidate")
        if candidate in candidates and candidates != None and candidate != None:
            alert = "Please dont repeat the candidates!!"
            return redirect('candidates',alert)
        if candidate != None:
            candidates[candidate] = 0
        return redirect('add_candidates')
    else:
        if alert != '' and candidates != None:
            return render(request,"add_candidates.html",{'candidates':candidates,'alert':alert})    
        if candidates:
            return render(request,"add_candidates.html",{'candidates':candidates})
        else:
            return render(request,"add_candidates.html")

def poll(request,alert = ''):
    if request.method == "POST":
        id = request.POST.get("id")
        candidate = request.POST.get("poll_value")
        if candidate == None:
            alert = "Select one candidate and then submit!!"
            return redirect('poll1',alert)
        if id in ids and ids != None and id != None:
            alert = "You have voted already!!"
            return redirect('poll1',alert)
        if id != None:
            ids.append(id)
            candidates[candidate] += 1
        return redirect('poll')
    else:
        if alert != '' and candidates != None:
            print(candidates)
            return render(request,"poll.html",{'candidates':candidates,'alert':alert})
        if candidates:
            return render(request,"poll.html",{'candidates':candidates})
        else:
            msge = "No candidates had been added yet!!"
            print(msge)
            return render(request,"poll.html",{'msge':msge})

def votingSummary(request):
    if candidates:
        return render(request,"summary.html",{'candidates':candidates})
    else:
        msge = "No candidates had been added yet!!"
        return render(request,"summary.html",{'msge':msge})

def pollResult(request):
    if candidates:
        result= dict()
        cnt = 0
        sorted_dic = sorted(candidates,key = candidates.get,reverse=True)
        print("Sorted dic: ",sorted_dic," cnt = ",cnt)
        for i in sorted_dic:
            if cnt == 2:
                break
            else:
                result[i] = candidates[i]
                cnt+=1
        return render(request,"poll_result.html",{'candidates':result})
    else:
        msge = "No candidates had been added yet!!"
        return render(request,"poll_result.html",{'msge':msge})
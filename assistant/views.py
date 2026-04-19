from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Task
from .utils import analyze_vunoh_request

def dashboard(request):
    # Requirement 8: Task Dashboard [cite: 76-77]
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'assistant/dashboard.html', {'tasks': tasks})

def process_request(request):
    if request.method == "POST":
        user_text = request.POST.get('user_input')
        
        # Call AI Brain
        ai_results, risk_score, team = analyze_vunoh_request(user_text)
        
        # Save to DB [cite: 52-56, 70, 81]
        Task.objects.create(
            intent=ai_results['intent'],
            entities=ai_results['entities'],
            risk_score=risk_score,
            steps=ai_results['steps'],
            whatsapp_msg=ai_results['messages']['whatsapp'],
            email_msg=ai_results['messages']['email'],
            sms_msg=ai_results['messages']['sms'],
            assigned_to=team
        )
        return redirect('dashboard')

def update_status(request, task_id):
    # Requirement 8: Update status between Pending, In Progress, Completed [cite: 78-79]
    if request.method == "POST":
        task = Task.objects.get(id=task_id)
        task.status = request.POST.get('status')
        task.save()
        return JsonResponse({"status": "success"})
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns=[
    path('',views.HomeView.as_view(),name="homepage"),
    path('about/',views.AboutView.as_view(),name="aboutpage"),
    path('datatables/',views.DataTableView.as_view(),name="datatables"),
    path('signup/',views.SignUpView.as_view(),name="signuppage"),
    path('profile/',views.ProfileView.as_view(),name="profilepage"),
    path('logout/',views.UserLogOutView.as_view(),name="logoutuser"),
    path('delete/<int:id>',views.DeleteTask.as_view(),name="deletetask"),
    path('login/',views.user_login,name="loginpage"),
    path('changepass/',views.changepass,name="changepass"),
    path('update/<int:id>',views.update_task,name="updatetask"),

    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="enroll/password_reset.html"),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="enroll/password_reset_sent.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="enroll/password_reset_form.html"),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="enroll/password_reset_done.html"),name="password_reset_complete"),

    path('download/',views.some_view,name="download"),
]

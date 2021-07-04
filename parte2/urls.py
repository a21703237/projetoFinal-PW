from django.urls import path
from . import views
from .views import contacts_create_view, quiz_create_view, comments_create_view, quiz_nota_page_views

urlpatterns = [
    path('', views.index_page_views, name="index"),
    path('bottas', views.bottas_page_views, name="botas"),
    path('romeo', views.romeo_page_views, name="romeo"),
    path('alonso', views.alonso_page_views, name="alonso"),
    path('tauri', views.tauri_page_views, name="tauri"),
    path('alpine', views.alpine_page_views, name="alpine"),
    path('aston', views.aston_page_views, name="aston"),
    path('ferrari', views.ferrari_page_views, name="ferrari"),
    path('gasly', views.gasly_page_views, name="gasly"),
    path('giovinazzi', views.giovinazzi_page_views, name="giovinazzi"),
    path('haas', views.haas_page_views, name="haas"),
    path('hamilton', views.hamilton_page_views, name="hamilton"),
    path('latifi', views.latifi_page_views, name="latifi"),
    path('leclerc', views.leclerc_page_views, name="leclerc"),
    path('mazepin', views.mazepin_page_views, name="mazepin"),
    path('mclraren', views.mclaren_page_views, name="mclaren"),
    path('mercedes', views.mercedes_page_views, name="mercedes"),
    path('norris', views.norris_page_views, name="norris"),
    path('ocon', views.ocon_page_views, name="ocon"),
    path('perez', views.perez_page_views, name="perez"),
    path('raikkonen', views.raikkonen_page_views, name="raikkonen"),
    path('redbull', views.redbull_page_views, name="redbull"),
    path('ricciardo', views.ricciardo_page_views, name="ricciardo"),
    path('russel', views.russel_page_views, name="russel"),
    path('sainz', views.sainz_page_views, name="sainz"),
    path('schumacher', views.shumacher_page_views, name="schumacher"),
    path('standings', views.standings_page_views, name="standings"),
    path('stroll', views.strollpage_views, name="stroll"),
    path('tsunoda', views.tsunoda_page_views, name="tsunoda"),
    path('verstappen', views.verstappen_page_views, name="verstappen"),
    path('vettel', views.vettel_page_views, name="vettel"),
    path('williams', views.williams_page_views, name="williams"),
    path('about', views.about_page_views, name="about"),
    path('form', views.contact_form_page_views, name="form"),
    path('commentsForm', views.comments_form_page_views, name="commentsForm"),
    path('contactForm', contacts_create_view, name="contactForm"),
    path('quiz', quiz_create_view, name="quiz"),
    path('comments', comments_create_view, name="comments"),
    path('quizNota', quiz_nota_page_views, name="quizNota"),



]

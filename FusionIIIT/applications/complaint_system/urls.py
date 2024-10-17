
# complaint/urls.py
from django.urls import path
from .views import (
    CheckUser,
    UserComplaintView,
    CaretakerFeedbackView,
    SubmitFeedbackView,
    ComplaintDetailView,
)
from .views import (
    CaretakerLodgeView,
    CaretakerView,
    FeedbackCareView,
    ResolvePendingView,
    ComplaintDetailView,
    SearchComplaintView,
    SubmitFeedbackCaretakerView,
)
from .views import (
    SupervisorLodgeView,
    SupervisorView,
    FeedbackSuperView,
    CaretakerIdKnowMoreView,
    SupervisorComplaintDetailView,
    SupervisorResolvePendingView,
    SupervisorSubmitFeedbackView,
)

from django.urls import path
from .views import (
    RemoveWorkerView,
    AssignWorkerView,
    DeleteComplaintView,
    ChangeStatusView,
    ChangeStatusSuperView,
    # Other imported views
)



app_name = "complaint"

urlpatterns = [
    path("", CheckUser.as_view(), name="complaint"),
    path("user/", UserComplaintView.as_view(), name="user-complaints"),
    path("user/caretakerfb/", CaretakerFeedbackView.as_view(), name="caretaker-feedback"),
    path("user/<int:complaint_id>/", SubmitFeedbackView.as_view(), name="submit-feedback"),
    path("user/detail/<int:detailcomp_id1>/", ComplaintDetailView.as_view(), name="detail"),
    # Other URL patterns
    path('caretaker/lodge/', CaretakerLodgeView.as_view()),  # Converted to DRF
    path('caretaker/', CaretakerView.as_view(), name='caretaker'),  # check
    path('caretaker/feedback/<int:feedcomp_id>/', FeedbackCareView.as_view()),  # Converted to DRF
    path('caretaker/pending/<int:cid>/', ResolvePendingView.as_view()),  # Converted to DRF
    path('caretaker/detail2/<int:detailcomp_id1>/', ComplaintDetailView.as_view()),  # Converted to DRF
    path('caretaker/search_complaint', SearchComplaintView.as_view()),  # Converted to DRF
    path('caretaker/<int:complaint_id>/feedback/', SubmitFeedbackCaretakerView.as_view()),  # Converted to DRF
        # Supervisor URLs
    path('supervisor/lodge/', SupervisorLodgeView.as_view()),
    path('supervisor/', SupervisorView.as_view()), #check
    path('supervisor/feedback/<int:feedcomp_id>/', FeedbackSuperView.as_view()),
    path('supervisor/caretaker_id_know_more/<int:caretaker_id>/', CaretakerIdKnowMoreView.as_view()),
    
]

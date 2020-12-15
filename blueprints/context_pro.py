def styles(label):
  pass
  gallery = {  # font awesome icons for member forms
    "approved": "primary",
    "pending": "info",
    "denied": "danger",
    "delivered": "warning",
    "received": "warning",
    "withdrew": "danger",
  }
  return gallery.get(label, 'secondary')

def fa_icons(label):
  pass
  gallery = {  # font awesome icons for member forms
    "email": "s fa-envelope",
    "username": "r fa-user-circle",
    "picture": "s fa-image",
    "first_name": "s fa-user-edit",
    "gender": "s fa-venus-mars",
    "id": "s fa-id-card",
    "image_file": "s fa-file-image",
    "img_url": "s fa-image",
    "instagram": "b fa-instagram",
    "is_admin": "s fa-user-md",
    "is_member": "s fa-user-shield",
    "is_prez": "s fa-user-graduate",
    "last_name": "s fa-user-edit",
    "linkedin": "b fa-linkedin",
    "middle_name": "s fa-question-circle",
    "phone_num": "s fa-phone",
    "twitter": "b fa-twitter",
    "user_id": "s fa-user-tag",
    "menu": "s fa-sort",
    "new_note": "s fa-sticky-note",
    "display_requests": "b fa-tripadvisor",
    "make_admin": "s fa-user-md",
    "make_member": "s fa-user-check",
    "make_prez": "s fa-user-graduate",
    "admin_request":  "s fa-concierge-bell",
    "member_request": "s fa-concierge-bell",
    "prez_request":   "s fa-concierge-bell",
    "delivered":   "s fa-envelope",
    "denied":   "s fa-gavel",
    "approved":   "s fa-stamp",
    "pending":  "s fa-balance-scale",
    "date_posted": "r fa-calendar-alt",
    "note_content": "r fa-paper-plane",
    "req_content": "r fa-envelope-open",
    'member' : 's fa-user-check',
    'admin' : 's fa-user-md',
    'prez' : 's fa-user-graduate',
  }
  return gallery.get(label, 's fa-edit')

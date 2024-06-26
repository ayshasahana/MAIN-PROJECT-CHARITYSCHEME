from django.contrib.auth import admin
from django.urls import path


from Charity_Scheme import views

urlpatterns = [

    path('', views.first, name='first'),
    path('login', views.login, name='login'),
    path('registration', views.registration, name='registration'),
    path('logincode', views.logincode, name='logincode'),
    path('Registration', views.Registration, name="Registration"),
    path('reg', views.reg, name="reg"),
    path('adminhomepage', views.adminhomepage, name="adminhomepage"),
    path('department_homepage_sub', views.department_homepage_sub, name="department_homepage_sub"),
    path('mngdepartment', views.mngdepartment, name="mngdepartment"),
    path('adddepatment', views.adddepatment, name="adddepatment"),
    path('adddepcode', views.adddepcode, name="adddepcode"),
    path('editdep/<int:id>', views.editdep, name="editdep"),
    path('editdepcode', views.editdepcode, name="editdepcode"),
    path('deletedep/<int:id>', views.deletedep, name="deletedep"),
    path('searchdep', views.searchdep, name="searchdep"),
    path('mngfoodchart', views.mngfoodchart, name="mngfoodchart"),
    path('addfoodchart', views.addfoodchart, name="addfoodchart"),
    path('mngproduct', views.mngproduct, name="mngproduct"),
    path('add_product', views.add_product, name="add_product"),
    path('verify_need', views.verify_need, name="verify_need"),
    path('view_foodchart_and_donation_details', views.view_foodchart_and_donation_details, name="view_foodchart_and_donation_details"),
    path('view_need_and_donate_details', views.view_need_and_donate_details, name="view_need_and_donate_details"),
    path('view_order_history', views.view_order_history, name="view_order_history"),
    path('view_patient_information', views.view_patient_information, name="view_patient_information"),
    path('view_volunteer', views.view_volunteer, name="view_volunteer"),
    path('generate_report', views.generate_report, name="generate_report"),



    path('department_homepage', views.department_homepage, name="department_homepage"),
    path('add_and_manage_inventory', views.add_and_manage_inventory, name="add_and_manage_inventory"),
    path('add_inventory', views.add_inventory, name="add_inventory"),
    path('add_and_manage_needs', views.add_and_manage_needs, name="add_and_manage_needs"),
    path('addneedcode', views.addneedcode, name="addneedcode"),
    path('add_needs', views.add_needs, name="add_needs"),
    path('editneeds/<int:id>', views.editneeds, name="editneeds"),
    path('deleteneeds/<int:id>', views.deleteneeds, name="deleteneeds"),
    path('editcode1', views.editcode1, name="editcode1"),
    path('add_and_manage_volunteer', views.add_and_manage_volunteer, name="add_and_manage_volunteer"),
    path('add_volunteer', views.add_volunteer, name="add_volunteer"),
    path('editvol/<int:id>', views.editvol, name="editvol"),
    path('editvol1', views.editvol1, name="editvol1"),
    path('editcode', views.editcode, name="editcode"),
    path('verify_user_request', views.verify_user_request, name="verify_user_request"),
    path('accept/<int:id>', views.accept, name="accept"),
    path('reject/<int:id>', views.reject, name="reject"),
    path('search_add_and_manage_needs', views.search_add_and_manage_needs, name="search_add_and_manage_needs"),



    path('user_homepage', views.user_homepage, name="user_homepage"),
    path('request_for_inventory', views.request_for_inventory, name="request_for_inventory"),
    path('view_foodchart_and_donate', views.view_foodchart_and_donate, name="view_foodchart_and_donate"),
    path('view_need_and_donate', views.view_need_and_donate, name="view_need_and_donate"),
    path('view_Product_and_purchase', views.view_Product_and_purchase, name="view_Product_and_purchase"),
    path('view_more_product/<int:id>', views.view_more_product, name="view_more_product"),
    path('view_item_product/<int:id>', views.view_item_product, name="view_item_product"),
    path('view_my_order', views.view_my_order, name="view_my_order"),
    path('view_my_cart', views.view_my_cart, name="view_my_cart"),
    path('view_more', views.view_more, name="view_more"),
    path('view_item', views.view_item, name="view_item"),
    path('addtocart', views.addtocart, name="addtocart"),
    path('myreq', views.myreq, name="myreq"),
    path('ordrprdctcode', views.ordrprdctcode, name="ordrprdctcode"),
    path('product_userpayy', views.product_userpayy, name="product_userpayy"),
    path('product_userpayy1', views.product_userpayy1, name="product_userpayy1"),
    path('oredercartproduct', views.oredercartproduct, name="oredercartproduct"),
    path('search_order_history', views.search_order_history, name="search_order_history"),





    path('volunteer_homepage', views.volunteer_homepage, name="volunteer_homepage"),
    path('add_and_manage_patientinfo', views.add_and_manage_patientinfo, name="add_and_manage_patientinfo"),
    path('add_patients', views.add_patients, name="add_patients"),
    path('product_stock_update', views.product_stock_update, name="product_stock_update"),
    path('update_stock', views.update_stock, name="update_stock"),
    path('view_assigned_department', views.view_assigned_department, name="view_assigned_department"),
    path('addvolcode', views.addvolcode, name="addvolcode"),
    path('searchvol', views.searchvol, name="searchvol"),
    path('deletevol/<int:id>', views.deletevol, name="deletevol"),
    path('deletepai/<int:id>', views.deletepai, name="deletepai"),
    path('enabelevol/<int:id>', views.enabelevol, name="enabelevol"),
    path('enabelepai/<int:id>', views.enabelepai, name="enabelepai"),
    path('accept_need/<int:id>', views.accept_need, name="accept_need"),
    path('view_department', views.view_department, name="view_department"),
    path('searchvol', views.searchvol, name="searchvol"),
    path('user_pay_proceed',views.user_pay_proceed,name="user_pay_proceed"),
    path('on_payment_success/<int:id>/<str:id2>/<str:id3>', views.on_payment_success, name="on_payment_success"),
    path('on_payment_success4/<int:id>/<str:id2>/<str:id3>', views.on_payment_success4, name="on_payment_success4"),
    path('view_volunteersearch', views.view_volunteersearch, name="view_volunteersearch"),
    path('verify_needsearch', views.verify_needsearch, name="verify_needsearch"),
    path('check_email', views.check_email, name="check_email"),
    path('check_email1', views.check_email1, name="check_email1"),
    path('search_dep', views.search_dep, name="search_dep"),

    path('send_need_response/<int:id>', views.send_need_response, name="send_need_response"),
    path('getAmount', views.getAmount, name="getAmount"),
    path('addinvcode', views.addinvcode, name="addinvcode"),
    path('addfoodchart', views.addfoodchart, name="addfoodchart"),
    path('search1', views.search1, name="search1"),
    path('addpatientinfo', views.addpatientinfo, name="addpatientinfo"),
    path('addfoodchart_code', views.addfoodchart_code, name="addfoodchart_code"),
    path('editfoodchart/<int:id>', views.editfoodchart, name="editfoodchart"),
    path('deletefoodchart/<int:id>', views.deletefoodchart, name="deletefoodchart"),
    path('editcode_foodchart', views.editcode_foodchart, name="editcode_foodchart"),
    path('view_foodchart_add', views.view_foodchart_add, name="view_foodchart_add"),
    path('search_need_and_donate_details', views.search_need_and_donate_details, name="search_need_and_donate_details"),
    # path('editpatient', views.editpatient, name="editpatient"),
    path('editpatient1/<int:id>', views.editpatient1, name="editpatient1"),
    path('editpatientcode', views.editpatientcode, name="editpatientcode"),
    path('food_userpay', views.food_userpay, name="food_userpay"),
    path('on_payment_success1/<str:id>/<str:amt>', views.on_payment_success1, name="on_payment_success1"),
    path('deletepatient/<int:id>', views.deletepatient, name="deletepatient"),
    path('view_food_details/<int:id>', views.view_food_details, name="view_food_details"),
    path('searchpatient', views.searchpatient, name="searchpatient"),
    path('editinvcode', views.editinvcode, name="editinvcode"),
    path('edit_inv1/<int:id>', views.edit_inv1, name="edit_inv1"),
    path('delete_inv/<int:id>', views.delete_inv, name="delete_inv"),
    path('req_inv/<int:id>', views.req_inv, name="req_inv"),
    path('request_inv', views.request_inv, name="request_inv"),
    path('addproductcode', views.addproductcode, name="addproductcode"),
    path('food_userpayy', views.food_userpayy, name="food_userpayy"),
    path('transaction_history', views.transaction_history, name="transaction_history"),
    path('editproduct/<int:id>', views.editproduct, name="editproduct"),
    path('editproductcode', views.editproductcode, name="editproductcode"),
    path('delete_product/<int:id>', views.delete_product, name="delete_product"),
    path('deleteviewproduct/<int:id>/<int:qid>', views.deleteviewproduct, name="deleteviewproduct"),

    path('updatepro/<int:id>', views.updatepro, name="updatepro"),
    path('updateprocode', views.updateprocode, name="updateprocodes"),
    path('viewmore', views.viewmore, name="viewmore"),
    path('search_inv', views.search_inv, name="search_inv"),
    path('search_verify_user_request', views.search_verify_user_request, name="search_verify_user_request"),
    path('view_patient_information_search', views.view_patient_information_search, name="view_patient_information_search"),
    path('add_and_manage_inventory_search', views.add_and_manage_inventory_search, name="add_and_manage_inventory_search"),
    path('generate_report', views.generate_report, name="generate_report"),
    path('search_generate_report', views.search_generate_report, name="search_generate_report"),
    path('search_product', views.search_product, name="search_product"),
    path('search_donation_date', views.search_donation_date, name="search_donation_date"),
    path('disable_patientinfo', views.disable_patientinfo, name="disable_patientinfo"),

    path('add_reson', views.add_reson, name="add_reson"),
    path('view_reson', views.view_reson, name="view_reson"),
    path('view_foodchart_donation_details', views.view_foodchart_donation_details, name="view_foodchart_donation_details"),
    # path('request_for_inventory_search', views.request_for_inventory_search, name="request_for_inventory_search"),

]

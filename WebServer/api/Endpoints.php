<?php
    $gateway_host = 'http://127.0.0.1';
    $gateway_port = '5000';
    $url = $gateway_host.':'.$gateway_port.'/api';

    $login_api = $url.'/auth/login';
    
    $get_profiles_pages_api = $url.'/employee/page';
    $get_profiles_api = $url.'/employee';
    $get_profile_by_id_api = $url.'/employee/';
    $update_profiles_api = $url.'/employee/';
    $deactivate_profile_api = $url.'/employee/';

    $get_leaves_api = $url.'/leave';
    $get_leave_requests_api = $url.'/leave/request';
    $get_leave_pages_api = $url.'/leave/page';
    $get_leave_request_pages_api = $url.'/leave/request/page';
    $accept_leave_api = $url.'/leave/request/';
    $deny_leave_api = $url.'/leave/request/';
    $request_leave_api = $url.'/leave/request';

    $get_wfhs_api = $url.'/wfh';
    $get_wfh_requests_api = $url.'/wfh/request';
    $get_wfh_pages_api = $url.'/wfh/page';
    $get_wfh_request_pages_api = $url.'/wfh/request/page';
    $accept_wfh_api = $url.'/wfh/request/';
    $deny_wfh_api = $url.'/wfh/request/';
    $request_wfh_api = $url.'/wfh/request';

    $get_employee_current_attendance_api = $url.'/attendance/employee/';
    $check_in_api = $url.'/attendance/check-in';
    $check_out_api = $url.'/attendance/check-out';

    $get_timesheets_api = $url.'/timesheet';
    $get_timesheet_update_requests_api = $url.'/timesheet/request';
    $get_timesheet_pages_api = $url.'/timesheet/page';
    $get_timesheet_update_request_pages_api = $url.'/timesheet/request/page';
    $get_timesheet_by_id_api = $url.'/timesheet/';
    $update_timesheet_by_id_api = $url.'/timesheet/'; 
    $accept_update_timesheet_api = $url.'/timesheet/request/'; 
    $deny_update_timesheet_api = $url.'/timesheet/request/'; 
    $request_update_timesheet_api = $url.'/timesheet/request';
?>
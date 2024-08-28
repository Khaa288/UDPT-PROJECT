<?php
    $gateway_host = 'http://127.0.0.1';
    $gateway_port = '3000';
    $url = $gateway_host.':'.$gateway_port.'/api';

    $login_api = $url.'/auth/login';
    
    $get_profiles_pages_api = $url.'/employee/page';
    $get_profiles_api = $url.'/employee';
    $update_profiles_api = $url.'/employee/';
    $deactivate_profile_api = $url.'/employee/';

    $get_leaves_api = $url.'/leave';
    $get_leave_requests_api = $url.'/leave/request';
    $get_leave_pages_api = $url.'/leave/page';
    $get_leave_request_pages_api = $url.'/leave/page';
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
?>
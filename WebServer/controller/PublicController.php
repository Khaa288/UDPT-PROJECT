<?php 
class PublicController
{
    public function login(){
        require("./api/Endpoints.php");

        $api = $login_api;

        $request_body = array(
            'Username' => $_REQUEST["username"],
            'Password' => $_REQUEST["password"]
        );

        $response = ApiRequest::post($api, null, $request_body);

        if (!is_null($response)) {
            $_SESSION["AuthUser"] = json_encode($response);

            if ($response->Role == 'Manager') {
                $VIEW = "./view/ManagerDashboard.phtml";
            }

            else if ($response->Role == 'Employee') {
                $VIEW = "./view/EmployeeDashboard.phtml";
            }
            
            else {
                $VIEW = "./view/EmployeeDashboard.phtml";
            }

            require("./template/Layout.phtml");
        }
        else {
            PublicController::toLogin();
        }
    }

    public function toHome()
    {
        $VIEW = "./view/ManagerDashboard.phtml";
        require("./template/Layout.phtml");
    }

    public function toLogin() {
        $VIEW = "./view/LoginPage.phtml";
        require($VIEW);
    }

    public function toProfile() {
        require("./api/Endpoints.php");

        $pages = ApiRequest::get($get_profiles_pages_api, null);
        
        $profiles = ApiRequest::get($get_profiles_api, array(
            'page' => $_GET["page"],
            'pageSize' => $_GET["pageSize"]
        ));

        $VIEW = "./view/ProfileManagement/ListProfiles.phtml";
        require("./template/Layout.phtml");
    }

    public function toTimesheet() {
        $VIEW = "./view/TimesheetManagement/ListTimesheets.phtml";
        require("./template/Layout.phtml");
    }

    public function toLeave() {
        require("./api/Endpoints.php");

        $pages = ApiRequest::get($get_leave_pages_api, null);

        $leaves = ApiRequest::get($get_leaves_api, array(
            'page' => $_GET["page"],
            'pageSize' => $_GET["pageSize"]
        ));

        $VIEW = "./view/LeaveManagement/ListLeave.phtml";
        require("./template/Layout.phtml");
    }

    public function toLeaveRequest() {
        require("./api/Endpoints.php");

        $pages = ApiRequest::get($get_leave_request_pages_api, null);

        $leave_requests = ApiRequest::get($get_leave_requests_api, array(
            'page' => $_GET["page"],
            'pageSize' => $_GET["pageSize"]
        ));

        $VIEW = "./view/LeaveManagement/ListLeaveRequests.phtml";
        require("./template/Layout.phtml");
    }

    public function toWFH() {
        require("./api/Endpoints.php");

        $pages = ApiRequest::get($get_wfh_pages_api, null);

        $wfhs = ApiRequest::get($get_wfhs_api, array(
            'page' => $_GET["page"],
            'pageSize' => $_GET["pageSize"]
        ));

        $VIEW = "./view/WFHManagement/ListWFH.phtml";
        require("./template/Layout.phtml");
    }

    public function toWFHRequest() {
        require("./api/Endpoints.php");

        $pages = ApiRequest::get($get_wfh_request_pages_api, null);

        $wfh_requests = ApiRequest::get($get_wfh_requests_api, array(
            'page' => $_GET["page"],
            'pageSize' => $_GET["pageSize"]
        ));

        $VIEW = "./view/WFHManagement/ListWFHRequests.phtml";
        require("./template/Layout.phtml");
    }
}
?>
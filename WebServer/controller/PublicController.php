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
            $VIEW = "./view/ManagerDashboard.phtml";
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
        $VIEW = "./view/ProfileManagement/ListProfiles.phtml";
        require("./template/Layout.phtml");
    }

    public function toTimesheet() {
        $VIEW = "./view/TimesheetManagement/ListTimesheets.phtml";
        require("./template/Layout.phtml");
    }

    public function toLeave() {
        $VIEW = "./view/LeaveManagement/ListLeaveRequests.phtml";
        require("./template/Layout.phtml");
    }

    public function toWFH() {
        $VIEW = "./view/WFHManagement/ListWFHRequests.phtml";
        require("./template/Layout.phtml");
    }
}
?>
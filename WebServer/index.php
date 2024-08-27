<?php
session_start();
require_once("./controller/PublicController.php");
require_once("./controller/TimesheetController.php");
require_once("./api/ApiRequest.php");

$action = "";
if (isset($_REQUEST["action"])) {
    $action = $_REQUEST["action"];
}

switch ($action) {
    case "login":
        $controller = new PublicController();
        $controller->login();
        break;
    case "home":
        $controller = new PublicController();
        $controller->toHome();
        break;
    case "profile-management":
        $controller = new PublicController();
        $controller->toProfile();
        break;
    case "leave-management":
        $controller = new PublicController();
        $controller->toLeave();
        break;
    case "wfh-management":
        $controller = new PublicController();
        $controller->toWFH();
        break;
    case "timesheet-management":
        $controller = new PublicController();
        $controller->toTimesheet();
        break;
    case "timesheet-detail":
        $controller = new TimesheetController();
        $controller->toTimesheetDetail();
        break;

    default:
        unset($_SESSION["AuthUser"]);  
        $controller = new PublicController();
        $controller->toLogin();
}

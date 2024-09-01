<?php 
class WfhController
{
    public function acceptWfh()
    {
        require("./api/Endpoints.php");
        $requestId = $_REQUEST["requestId"];

        $response = ApiRequest::post($accept_wfh_api.$requestId.'/accept', null, null);

        header("Location: index.php?action=wfh-management&page=1&pageSize=5");
    }

    public function denyWfh()
    {
        require("./api/Endpoints.php");
        $requestId = $_REQUEST["requestId"];

        $response = ApiRequest::post($deny_wfh_api.$requestId.'/deny', null, null);

        $role = json_decode($_SESSION["AuthUser"])->Role;

        if ($role == 'Employee') {
            header("Location: index.php?action=employee-wfh-request-management&page=1&pageSize=5");
        }
        else if ($role == 'Manager') {
            header("Location: index.php?action=wfh-request-management&page=1&pageSize=5");
        }

        else {
            header("Location: index.php?action=logout");
        }
    }

    public function applyWfh()
    {
        require("./api/Endpoints.php");

        $employee_id = json_decode($_SESSION["AuthUser"])->EmployeeId;

        $employee = ApiRequest::get($get_profile_by_id_api.$employee_id, null, null);

        $request_employee = array(
            'EmployeeId' => $employee->EmployeeId,
            'EmployeeName' => $employee->FirstName . ' ' . $employee->MiddleName . ' ' . $employee->LastName,
            'EmployeeIdCardNum' => $employee->IdCardNum,
            'EmployeeJobTitle' => $employee->JobTitle
        );

        $date = date("d-m-Y", strtotime($_REQUEST["date"]));
        $wfh_type = $_REQUEST["wfhType"];
        $note = $_REQUEST["note"];

        $body = array(
            'Employee' => $request_employee,
            'Date' => $date,
            'WfhType' => $wfh_type,
            'Note' => $note
        );

        $response = ApiRequest::post($request_wfh_api, null, $body);

        header("Location: index.php?action=employee-wfh-request-management&page=1&pageSize=5");
    }
}
?>
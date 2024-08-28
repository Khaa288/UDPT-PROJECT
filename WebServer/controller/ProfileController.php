<?php 
class ProfileController
{
    public function updateProfile()
    {
        require("./api/Endpoints.php");

        $employeeId = $_REQUEST["employeeId"];

        echo $_REQUEST["firstName"];
        echo $_REQUEST["middleName"];
        $body = array(
            "FirstName" => $_REQUEST["firstName"],
            "MiddleName" => $_REQUEST["middleName"],
            "LastName" => $_REQUEST["lastName"],
            "Address" => $_REQUEST["address"],
            "IdCardNum" => $_REQUEST["idCardNum"],
            "TaxNum" => $_REQUEST["taxNum"],
            "BankAccountNum" => $_REQUEST["bankAccountNum"],
            "Gender" => $_REQUEST["gender"],
            "JobTitle" => $_REQUEST["jobTitle"],
            "PhoneNum" => $_REQUEST["phoneNum"]
        );

        ApiRequest::put($update_profiles_api.$employeeId, null, $body);

        header("Location: index.php?action=profile-management&page=1&pageSize=5");
    }

    public function deactivateProfile() 
    {
        require("./api/Endpoints.php");

        $employeeId = $_REQUEST["employeeId"];

        ApiRequest::post($deactivate_profile_api.$employeeId.'/deactivate', null, null);

        header("Location: index.php?action=profile-management&page=1&pageSize=5");
    }
}
?>
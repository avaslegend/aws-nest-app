from datetime import datetime

class Template:

    PROJECT_MAIL = "SAVA PE"
    DESCRIPTION_MAIL = "An error has occurred in the {PROJECT_MAIL} {PROCESS} processing. Check the Log Message."
    RECOMMEND_MAIL = "Review the error in the {PROCESS} process Log path."

    def __init__(self, process):
        self.RECOMMEND_MAIL = self.RECOMMEND_MAIL.replace("{PROCESS}", process)
        self.DESCRIPTION_MAIL = self.DESCRIPTION_MAIL.replace("{PROCESS}", process)
        self.DESCRIPTION_MAIL = self.DESCRIPTION_MAIL.replace("{PROJECT_MAIL}", self.PROJECT_MAIL)
        self.PROCESS = process

    def getFormatDateNow(self):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M")
        return dt_string

    def getHtmlMailBrandliveGray(self, ERROR_MESSAGE):
        font_size_family_tbody = " {font-family: Calibri Bold,Tohama,sans-serif; font-size: 0.9em;}"
        font_size_family_tfooter = " {font-family: Calibri Bold,Tohama,sans-serif; font-size: 0.91em;}"
        padding_table = " {padding: 4px;}"
        DATE_NOW_MAIL = self.getFormatDateNow()

        BODY_HTML_TEMPLATE = f"""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    
    <title>Correo de log errores</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        tbody {font_size_family_tbody}
        tfoot {font_size_family_tfooter}
         table th, table td{padding_table}
    </style>
</head>
<body>
    <table align="center" width="100%" border="0px" cellspacing="0" cellpadding="0">
        <tbody>
            <tr>
                <td align="center">
                    <table width="750" cellpadding="0" border="0" cellspacing="0" style="border:0.5px solid;border-radius:10px;color: #b0c3cf;">
                        <thead>
                            <tr>
                                <th colspan="4">
                                    
<table width="100%" cellpadding="0" border="0" cellspacing="0" style="background-image: linear-gradient(#455560, #FFFFFF);color: #ffffff;border-radius: 10px;height: 125px;">
                                        <tbody><tr>
                                            <td width="30%" style="text-align: right;">
                                                <img alt="Logo Summa Solutions" height="40px" width="126px" src="https://brandlivecommerce.com/assets/img/logo.svg">
                                            </td>
                                            <td width="70%">
                                                <div style="font-size: 2.1em;padding-right: 186px;">SUPPORT MESSAGE</div>
                                            </td>
                                        </tr>
                                    </tbody></table>
                                </th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td width="3%"></td>
                                <td width="92%" colspan="2">
                                    <table width="100%" cellpadding="0" border="0" cellspacing="0" style="border:0.5px solid;color: #b0c3cf;border-radius:5px;font-size:1.2em;">
                                        <tbody>
                                            <tr>
                                                <td colspan="4" style="text-align: center;">
                                                    <b style="color: #455560;font-size: 1.5em;font-family: Calibri Bold,Tohama,sans-serif;">{self.PROJECT_MAIL} Error Summary</b>
                                                </td>
                                            </tr>
                                            <tr>
                                                <td></td>
                                                <td colspan="2" style="text-align:justify;font-size:12px;padding: 13px;color: #455560;"> {self.DESCRIPTION_MAIL}</td>
                                                <td></td>
                                            </tr>
                                            <tr>
                                                <td></td>
                                                <td><b style="padding-left: 13px;font-size: 1.2em;color: #455560;">Project:</b></td>
                                                <td style="color: #455560;font-size: 1em;font-family: Calibri Bold,Tohama,sans-serif;height: 30px;">{self.PROJECT_MAIL}</td>
                                                <td></td>
                                            </tr>
                                            <tr>
                                                <td></td>
                                                <td><b style="padding-left: 13px;font-size: 1.2em;color: #455560;">Date:</b></td>
                                                <td style="color: #455560;font-size: 1em;font-family: Calibri Bold,Tohama,sans-serif;height: 30px;">{DATE_NOW_MAIL}</td>
                                                <td></td>
                                            </tr>
                                            <tr>
                                                <td></td>
                                                <td><b style="padding-left: 13px;font-size: 1.2em;color: #455560;">Recommend:</b></td>
                                                <td style="color: #455560;font-size: 1em;font-family: Calibri Bold,Tohama,sans-serif;height: 30px;">{self.RECOMMEND_MAIL}</td>
                                                <td></td>
                                            </tr>
                                            <tr>
                                                <td></td>
                                                <td width="130"><b style="padding-left: 13px;font-size: 1.2em;color: #455560;"> Log Message: </b></td>
                                                <td style="color: #455560;font-family: Calibri Bold,Tohama,sans-serif;height: 30px;font-size: 1em;">{ERROR_MESSAGE}</td>
                                                <td></td>
                                            </tr>
                                            <tr>
                                                <td height="5"></td>
                                                <td> <b></b></td>
                                                <td></td>
                                                <td></td>
                                            </tr>
                                            <tr>
                                                <td></td>
                                                <td colspan="2" style="color:#c9c9c9;font-size:10px;text-align:justify;padding: 13px;">
                                                    This message is only addressed to its addressee and it could contain privileged and confidential information. If you are not the addressee indicated, you are advised that the utilization, divulgation and/or copy of this message without authorisation are prohibited by the legislation in force. If you have received this message by mistake, please notify us immediately by reply e-mail and delete this message. According to the Personal Data Protection Law, We inform you that your personal data are included in an automated file of responsibility of Summa Solutions. If you do not want keep on receiving information by means of e-mail and/or you desire to exercise your rights of access, rectification, cancellation and/or opposition regarding to your personal data, you can do them sending e-mail to <a href="mailto:pgomez@summasolutions.net" target="_blank">svazquez@infracommerce.lat</a>
                                                </td>
                                                <td></td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                                <td width="5%"></td>
                            </tr>
                        </tbody>
                        <tfoot style="
    color: #455560;
">
                            <tr>
                                <td height="20"></td>
                                <td></td>
                                <td></td>
                                <td></td>
                            </tr>
                            <tr>
                            <td width="20%" rowspan="4" colspan="2" style="padding-right:13px">
                                <table width="100%" cellpadding="0" border="0px" cellspacing="0" style="font-size:1.8em;font-weight:bold">
                                    <tbody><tr>
                                        <td rowspan="2" style="padding:0px;padding-right:8px;padding-left:10px">

                                            <img alt="Logo footer Summa Solutions" height="64px" width="200px" src="https://brandlivecommerce.com/assets/img/logo-footer.svg">
                                        </td>
                                        <td style="padding:0px">

                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="padding:0px">

                                        </td>
                                    </tr>
                                </tbody></table>
                            </td>
                            <td style="padding:0px;/* color: #3F3354; */">Brandlive - Infracommerce</td>
                            <td></td>
                            </tr>
                            <tr>
                            <td style="padding:0px;/* color: #3F3354; */"></td>
                            <td></td>
                            </tr>
                            <tr>
                            <td style="padding:0px"> <a href="https://brandlivecommerce.com/" target="_blank">https://brandlivecommerce.com</a> </td>
                            <td></td>
                            </tr>
                            <tr>
                                <td style="padding:0px;/* color: #3F3354; */">
                                    © 2023 Brandlive - Infracommerce
                                </td>
                                <td></td>
                            </tr>
                            <tr>
                                <td style="padding:0px"></td>
                                <td></td>
                                <td></td>
                                <td></td>
                            </tr>
                        </tfoot>
                    </table>
                </td>
            </tr>
        </tbody>
    </table>
</body></html>

                    """
        return BODY_HTML_TEMPLATE
    
    def getHtmlMailBrandliveRed(self, ERROR_MESSAGE):
        font_size_family_tbody = " {font-family: Calibri Bold,Tohama,sans-serif; font-size: 0.9em;}"
        font_size_family_tfooter = " {font-family: Calibri Bold,Tohama,sans-serif; font-size: 0.91em;}"
        padding_table = " {padding: 4px;}"
        DATE_NOW_MAIL = self.getFormatDateNow()

        BODY_HTML_TEMPLATE = f"""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    
    <title>Correo de log errores</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        tbody {font_size_family_tbody}
        tfoot {font_size_family_tfooter}
         table th, table td{padding_table}
    </style>
</head>
<body>
    <table align="center" width="100%" border="0px" cellspacing="0" cellpadding="0">
        <tbody>
            <tr>
                <td align="center">
                    <table width="750" cellpadding="0" border="0" cellspacing="0" style="border:0.5px solid;border-radius:10px;color: #efbdca;">
                        <thead>
                            <tr>
                                <th colspan="4">
                                    
<table width="100%" cellpadding="0" border="0" cellspacing="0" style="background-image: linear-gradient(#d11242, #FFFFFF);color: #ffffff;border-radius: 10px;height: 125px;">
                                        <tbody><tr>
                                            <td width="30%" style="text-align: right;">
                                                <img alt="Logo Summa Solutions" height="40px" width="126px" src="https://brandlivecommerce.com/assets/img/logo.svg">
                                            </td>
                                            <td width="70%">
                                                <div style="font-size: 2.1em;padding-right: 186px;">SUPPORT MESSAGE</div>
                                            </td>
                                        </tr>
                                    </tbody></table>
                                </th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td width="3%"></td>
                                <td width="92%" colspan="2">
                                    <table width="100%" cellpadding="0" border="0" cellspacing="0" style="border:0.5px solid;color: #efbdca;border-radius:5px;font-size:1.2em;">
                                        <tbody>
                                            <tr>
                                                <td colspan="4" style="text-align: center;">
                                                    <b style="color: #455560;font-size: 1.5em;font-family: Calibri Bold,Tohama,sans-serif;">{self.PROJECT_MAIL} Error Summary</b>
                                                </td>
                                            </tr>
                                            <tr>
                                                <td></td>
                                                <td colspan="2" style="text-align:justify;font-size:12px;padding: 13px;color: #455560;"> {self.DESCRIPTION_MAIL}</td>
                                                <td></td>
                                            </tr>
                                            <tr>
                                                <td></td>
                                                <td><b style="padding-left: 13px;font-size: 1.2em;color: #455560;">Project:</b></td>
                                                <td style="color: #455560;font-size: 1em;font-family: Calibri Bold,Tohama,sans-serif;height: 30px;">{self.PROJECT_MAIL}</td>
                                                <td></td>
                                            </tr>
                                            <tr>
                                                <td></td>
                                                <td><b style="padding-left: 13px;font-size: 1.2em;color: #455560;">Date:</b></td>
                                                <td style="color: #455560;font-size: 1em;font-family: Calibri Bold,Tohama,sans-serif;height: 30px;">{DATE_NOW_MAIL}</td>
                                                <td></td>
                                            </tr>
                                            <tr>
                                                <td></td>
                                                <td><b style="padding-left: 13px;font-size: 1.2em;color: #455560;">Recommend:</b></td>
                                                <td style="color: #455560;font-size: 1em;font-family: Calibri Bold,Tohama,sans-serif;height: 30px;">{self.RECOMMEND_MAIL} </td>
                                                <td></td>
                                            </tr>
                                            <tr>
                                                <td></td>
                                                <td width="130"><b style="padding-left: 13px;font-size: 1.2em;color: #455560;"> Log Message: </b></td>
                                                <td style="color: #455560;font-family: Calibri Bold,Tohama,sans-serif;height: 30px;font-size: 1em;">{ERROR_MESSAGE}</td>
                                                <td></td>
                                            </tr>
                                            <tr>
                                                <td height="5"></td>
                                                <td> <b></b></td>
                                                <td></td>
                                                <td></td>
                                            </tr>
                                            <tr>
                                                <td></td>
                                                <td colspan="2" style="color:#c9c9c9;font-size:10px;text-align:justify;padding: 13px;">
                                                    This message is only addressed to its addressee and it could contain privileged and confidential information. If you are not the addressee indicated, you are advised that the utilization, divulgation and/or copy of this message without authorisation are prohibited by the legislation in force. If you have received this message by mistake, please notify us immediately by reply e-mail and delete this message. According to the Personal Data Protection Law, We inform you that your personal data are included in an automated file of responsibility of Summa Solutions. If you do not want keep on receiving information by means of e-mail and/or you desire to exercise your rights of access, rectification, cancellation and/or opposition regarding to your personal data, you can do them sending e-mail to <a href="mailto:pgomez@summasolutions.net" target="_blank">svazquez@infracommerce.lat</a>
                                                </td>
                                                <td></td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                                <td width="5%"></td>
                            </tr>
                        </tbody>
                        <tfoot style="
    color: #455560;
">
                            <tr>
                                <td height="20"></td>
                                <td></td>
                                <td></td>
                                <td></td>
                            </tr>
                            <tr>
                            <td width="20%" rowspan="4" colspan="2" style="padding-right:13px">
                                <table width="100%" cellpadding="0" border="0px" cellspacing="0" style="font-size:1.8em;font-weight:bold">
                                    <tbody><tr>
                                        <td rowspan="2" style="padding:0px;padding-right:8px;padding-left:10px">

                                            <img alt="Logo footer Summa Solutions" height="64px" width="200px" src="https://brandlivecommerce.com/assets/img/logo-footer.svg">
                                        </td>
                                        <td style="padding:0px">

                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="padding:0px">

                                        </td>
                                    </tr>
                                </tbody></table>
                            </td>
                            <td style="padding:0px;/* color: #3F3354; */">Brandlive - Infracommerce</td>
                            <td></td>
                            </tr>
                            <tr>
                            <td style="padding:0px;/* color: #3F3354; */"></td>
                            <td></td>
                            </tr>
                            <tr>
                            <td style="padding:0px"> <a href="https://brandlivecommerce.com/" target="_blank">https://brandlivecommerce.com</a> </td>
                            <td></td>
                            </tr>
                            <tr>
                                <td style="padding:0px;/* color: #3F3354; */">
                                    © 2023 Brandlive - Infracommerce
                                </td>
                                <td></td>
                            </tr>
                            <tr>
                                <td style="padding:0px"></td>
                                <td></td>
                                <td></td>
                                <td></td>
                            </tr>
                        </tfoot>
                    </table>
                </td>
            </tr>
        </tbody>
    </table>
</body></html>

                    """
        return BODY_HTML_TEMPLATE
    
    def getHtmlMailInfracommerceCherry(self, ERROR_MESSAGE):
        font_size_family_tbody = " {font-family: Calibri Bold,Tohama,sans-serif; font-size: 0.9em;}"
        font_size_family_tfooter = " {font-family: Calibri Bold,Tohama,sans-serif; font-size: 0.91em;}"
        padding_table = " {padding: 4px;}"
        DATE_NOW_MAIL = self.getFormatDateNow()

        BODY_HTML_TEMPLATE = f"""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    
    <title>Correo de log errores</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        tbody {font_size_family_tbody}
        tfoot {font_size_family_tfooter}
         table th, table td{padding_table}
    </style>
</head>
<body>
    <table align="center" width="100%" border="0px" cellspacing="0" cellpadding="0">
        <tbody>
            <tr>
                <td align="center">
                    <table width="750" cellpadding="0" border="0" cellspacing="0" style="border:0.5px solid;border-radius:10px;color: #c4aee9;">
                        <thead>
                            <tr>
                                <th colspan="4">
                                    
<table width="100%" cellpadding="0" border="0" cellspacing="0" style="background-image: linear-gradient(#3F3354, #FFFFFF);color: #ffffff;border-radius: 10px;height: 125px;">
                                        <tbody><tr>
                                            <td width="30%" style="text-align: right;">
                                                <img alt="Logo Summa Solutions" height="40px" width="126px" src="https://www.infracommerce.com.br/image/infracommerce-w.svg">
                                            </td>
                                            <td width="70%">
                                                <div style="font-size: 2.1em;padding-right: 186px;">SUPPORT MESSAGE</div>
                                            </td>
                                        </tr>
                                    </tbody></table>
                                </th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td width="3%"></td>
                                <td width="92%" colspan="2">
                                    <table width="100%" cellpadding="0" border="0" cellspacing="0" style="border:0.5px solid;color: #ac98cd;border-radius:5px;font-size:1.2em;">
                                        <tbody>
                                            <tr>
                                                <td colspan="4" style="text-align: center;">
                                                    <b style="color: #3F3354;font-size: 1.5em;font-family: Calibri Bold,Tohama,sans-serif;">{self.PROJECT_MAIL} Error Summary</b>
                                                </td>
                                            </tr>
                                            <tr>
                                                <td></td>
                                                <td colspan="2" style="text-align:justify;font-size:12px;padding: 13px;color: #3F3354;">{self.DESCRIPTION_MAIL}</td>
                                                <td></td>
                                            </tr>
                                            <tr>
                                                <td></td>
                                                <td><b style="padding-left: 13px;font-size: 1.2em;color: #3F3354;">Project:</b></td>
                                                <td style="color: #3F3354;font-size: 1em;font-family: Calibri Bold,Tohama,sans-serif;height: 30px;">{self.PROJECT_MAIL}</td>
                                                <td></td>
                                            </tr>
                                            <tr>
                                                <td></td>
                                                <td><b style="padding-left: 13px;font-size: 1.2em;color: #3F3354;">Date:</b></td>
                                                <td style="color: #3F3354;font-size: 1em;font-family: Calibri Bold,Tohama,sans-serif;height: 30px;">{DATE_NOW_MAIL}</td>
                                                <td></td>
                                            </tr>
                                            <tr>
                                                <td></td>
                                                <td><b style="padding-left: 13px;font-size: 1.2em;color: #3F3354;">Recommend:</b></td>
                                                <td style="color: #3F3354;font-size: 1em;font-family: Calibri Bold,Tohama,sans-serif;height: 30px;">{self.RECOMMEND_MAIL}</td>
                                                <td></td>
                                            </tr>
                                            <tr>
                                                <td></td>
                                                <td width="130"><b style="padding-left: 13px;font-size: 1.2em;color: #3F3354;"> Log Message: </b></td>
                                                <td style="color: #3F3354;font-family: Calibri Bold,Tohama,sans-serif;height: 30px;font-size: 1em;">{ERROR_MESSAGE}</td>
                                                <td></td>
                                            </tr>
                                            <tr>
                                                <td height="5"></td>
                                                <td> <b></b></td>
                                                <td></td>
                                                <td></td>
                                            </tr>
                                            <tr>
                                                <td></td>
                                                <td colspan="2" style="color:#c9c9c9;font-size:10px;text-align:justify;padding: 13px;">
                                                    This message is only addressed to its addressee and it could contain privileged and confidential information. If you are not the addressee indicated, you are advised that the utilization, divulgation and/or copy of this message without authorisation are prohibited by the legislation in force. If you have received this message by mistake, please notify us immediately by reply e-mail and delete this message. According to the Personal Data Protection Law, We inform you that your personal data are included in an automated file of responsibility of Summa Solutions. If you do not want keep on receiving information by means of e-mail and/or you desire to exercise your rights of access, rectification, cancellation and/or opposition regarding to your personal data, you can do them sending e-mail to <a href="mailto:pgomez@summasolutions.net" target="_blank">svazquez@infracommerce.lat</a>
                                                </td>
                                                <td></td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                                <td width="5%"></td>
                            </tr>
                        </tbody>
                        <tfoot>
                            <tr>
                                <td height="20"></td>
                                <td></td>
                                <td></td>
                                <td></td>
                            </tr>
                            <tr>
                            <td width="20%" rowspan="4" colspan="2" style="padding-right:13px">
                                <table width="100%" cellpadding="0" border="0px" cellspacing="0" style="font-size:1.8em;font-weight:bold">
                                    <tbody><tr>
                                        <td rowspan="2" style="padding:0px;padding-right:8px;padding-left:10px">

                                            <img alt="Logo footer Summa Solutions" height="64px" width="200px" src="https://www.infracommerce.com.br/image/infracommerce.svg">
                                        </td>
                                        <td style="padding:0px">

                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="padding:0px">

                                        </td>
                                    </tr>
                                </tbody></table>
                            </td>
                            <td style="padding:0px;color: #3F3354;">Infracommerce</td>
                            <td></td>
                            </tr>
                            <tr>
                            <td style="padding:0px;color: #3F3354;"></td>
                            <td></td>
                            </tr>
                            <tr>
                            <td style="padding:0px"> <a href="https://www.infracommerce.com.br/" target="_blank">https://www.infracommerce.com.br</a> </td>
                            <td></td>
                            </tr>
                            <tr>
                                <td style="padding:0px;color: #3F3354;">
                                    © 2023 Infracommerce
                                </td>
                                <td></td>
                            </tr>
                            <tr>
                                <td style="padding:0px"></td>
                                <td></td>
                                <td></td>
                                <td></td>
                            </tr>
                        </tfoot>
                    </table>
                </td>
            </tr>
        </tbody>
    </table>
</body></html>

                    """
        return BODY_HTML_TEMPLATE

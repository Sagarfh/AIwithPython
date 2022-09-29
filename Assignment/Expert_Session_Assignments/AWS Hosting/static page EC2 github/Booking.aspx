<%@ Page Language="C#" AutoEventWireup="true" CodeFile="Booking.aspx.cs" Inherits="Booking" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
    <style type="text/css">
        .style1
        {
            width: 60%;
            height: 378px;
        }
    </style>
</head>
  <body bgcolor="teal">
	  <form id="form1" runat="server">
	<center>
	    <table border="1" bgcolor="wheat"  width="800">
	             <tr>
		 	<td>
		         <img src="banner.jpg"  width="900">	
	         	</td>
	             </tr>
	             <tr>
		 <td align="center">
		         <font size="5"><b>Utsav Rock Garden &nbsp Gotagodi, Tq: Shiggavi Dt: Haveri</b></font>	
	                    </td>
	             </tr>
	             <tr>
		 <td align="center">
		         <b>
			<a href="Home.html">Home</a>
			<a href="About.html">About Us</a>
			<a href="Gallery.html">Gallery</a>
			<a href="Activities.html">Activities</a>
			<a href="Contact.html">Contact</a>
		         </b>	
	                    </td>
	             </tr>
	             <tr>
		 <td>
		  <p>
 <font size="4">
		         <b>
Utsav Rock Garden</b></font></p>
             <p>
                 <table bgcolor="#00FFCC" border="1" class="style1">
                     <tr>
                         <td align="right">
                             Name of Visitor</td>
                         <td align="left">
                             <asp:TextBox ID="TextBox1" runat="server"></asp:TextBox>
                         </td>
                     </tr>
                     <tr>
                         <td align="right">
                             Address</td>
                         <td align="left">
                             <asp:TextBox ID="TextBox2" runat="server" TextMode="MultiLine"></asp:TextBox>
                         </td>
                     </tr>
                     <tr>
                         <td align="right">
                             Contact No</td>
                         <td align="left">
                             <asp:TextBox ID="TextBox3" runat="server"></asp:TextBox>
                         </td>
                     </tr>
                     <tr>
                         <td align="right">
                             No of Adults</td>
                         <td align="left">
                             <asp:DropDownList ID="DropDownList1" runat="server" AutoPostBack="True" 
                                 onselectedindexchanged="DropDownList1_SelectedIndexChanged">
                                 <asp:ListItem>1</asp:ListItem>
                                 <asp:ListItem>2</asp:ListItem>
                                 <asp:ListItem>3</asp:ListItem>
                                 <asp:ListItem>4</asp:ListItem>
                                 <asp:ListItem>5</asp:ListItem>
                             </asp:DropDownList>
                             <asp:TextBox ID="TextBox4" runat="server" ReadOnly="True">0</asp:TextBox>
                         </td>
                     </tr>
                     <tr>
                         <td align="right">
                             No of Children</td>
                         <td align="left">
                             <asp:DropDownList ID="DropDownList2" runat="server" AutoPostBack="True" 
                                 onselectedindexchanged="DropDownList2_SelectedIndexChanged">
                                 <asp:ListItem>1</asp:ListItem>
                                 <asp:ListItem>2</asp:ListItem>
                                 <asp:ListItem>3</asp:ListItem>
                                 <asp:ListItem>4</asp:ListItem>
                                 <asp:ListItem>5</asp:ListItem>
                             </asp:DropDownList>
                             <asp:TextBox ID="TextBox5" runat="server" ReadOnly="True">0</asp:TextBox>
                         </td>
                     </tr>
                     <tr>
                         <td align="right">
                             Room Type</td>
                         <td align="left">
                             <asp:DropDownList ID="DropDownList3" runat="server" AutoPostBack="True" 
                                 onselectedindexchanged="DropDownList3_SelectedIndexChanged">
                                 <asp:ListItem>Deluxe</asp:ListItem>
                                 <asp:ListItem>Semi Deluxe</asp:ListItem>
                                 <asp:ListItem>Economical</asp:ListItem>
                                 <asp:ListItem>Not Required</asp:ListItem>
                             </asp:DropDownList>
                             <asp:TextBox ID="TextBox6" runat="server" ReadOnly="True"></asp:TextBox>
                         </td>
                     </tr>
                     <tr>
                         <td align="right">
                             Activities Amount</td>
                         <td align="left">
                             <asp:TextBox ID="TextBox7" runat="server" ReadOnly="True">0</asp:TextBox>
                         </td>
                     </tr>
                     <tr>
                         <td align="right">
                             Total Amount (Act+Room)</td>
                         <td align="left">
                             <asp:TextBox ID="TextBox8" runat="server" ReadOnly="True">0</asp:TextBox>
                         </td>
                     </tr>
                     <tr>
                         <td align="center" colspan="2">
                             <asp:Button ID="BtnConfirm" runat="server" onclick="BtnConfirm_Click" 
                                 Text="Confirm" />
                             <asp:Button ID="BtnSubmit" runat="server" onclick="BtnSubmit_Click" 
                                 Text="Submit" />
                             <asp:Button ID="BtnReset" runat="server" onclick="BtnReset_Click" 
                                 Text="Reset" />
                         </td>
                     </tr>
                     <tr>
                         <td align="center" colspan="2">
                             <asp:Label ID="Label1" runat="server" Text="Label"></asp:Label>
                         </td>
                     </tr>
                 </table>
                 <font size="4">
		         <b>
<br>

		         </b>	
</p>
		  </p>
 </font>
	                    </td>
	             </tr>
	             <tr>
		 <td><marquee behavior="alternate">
		         <img src="1.jpg"  width="150" height="150">	
		         <img src="2.jpg"  width="150" height="150">	
		         <img src="3.jpg"  width="150" height="150">	
		         <img src="4.jpg"  width="150" height="150">	
		         <img src="5.jpg"  width="150" height="150">	
		         <img src="6.jpg"  width="150" height="150">	
		         <img src="7.jpg"  width="150" height="150">	
		         <img src="8.jpg"  width="150" height="150">	
		</marquee>
	                    </td>
	             </tr>
	             <tr>
		 <td>
		       <marquee scrollamount="10" behavior="alternate">  <b>
			<font size="4"><font face="Jokerman"><font color="red">DASNUR'S UTSAV ROCK GARDEN</font>
		         </b>	
		       </marquee>
	                    </td>
	             </tr>
	             <tr>
		 <td align="right">
		         <b>
			<a href="Home.html">Home</a>
			<a href="About.html">About Us</a>
			<a href="Gallery.html">Gallery</a>
			<a href="Activities.html">Activities</a>
			<a href="Contact.html">Contact</a>
		         </b>	
	                    </td>
	             </tr>
	    </table>
	</center>
      </form>
    </body>
</html>
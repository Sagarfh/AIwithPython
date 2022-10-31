using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Data.OleDb;
public partial class Booking : System.Web.UI.Page
{
    OleDbCommand cm;
    OleDbConnection db;
    String st = "";
    String cn = "";
    protected void Page_Load(object sender, EventArgs e)
    {
        cn = @"Provider=Microsoft.jet.oledb.4.0;data source=G:\ROCK.mdb";
        db = new OleDbConnection(cn);
        db.Open();
        if (Page.IsPostBack == false)
        {
            Label1.Text = "Please Fill up all the details and click on submit";
            BtnSubmit.Enabled = true;
            Label1.ForeColor = System.Drawing.Color.Red;
        }
    }
    protected void BtnReset_Click(object sender, EventArgs e)
    {
        TextBox1.Text = "";
        TextBox2.Text = "";
        TextBox3.Text = "";
        TextBox4.Text = "";
        TextBox5.Text = "";
        TextBox6.Text = "";
        TextBox7.Text = "";
        TextBox8.Text = "";
        TextBox1.Focus();
        Label1.Text = "Please Fill up all the details and click on submit";
        BtnSubmit.Enabled = true;

    }
    protected void DropDownList1_SelectedIndexChanged(object sender, EventArgs e)
    {
        if (DropDownList1.SelectedIndex == 0)
        {
            TextBox4.Text ="1000";

        }
        else if (DropDownList1.SelectedIndex == 1)
        {
            TextBox4.Text = "2000";

        }
        else if (DropDownList1.SelectedIndex == 2)
        {
            TextBox4.Text = "3000";

        }
        else if (DropDownList1.SelectedIndex == 3)
        {
            TextBox4.Text = "4000";

        }
        else
        {
            TextBox4.Text = "5000";

        }
    }
    protected void DropDownList2_SelectedIndexChanged(object sender, EventArgs e)
    {
        if (DropDownList2.SelectedIndex == 0)
        {
            TextBox5.Text = "500";

        }
        else if (DropDownList2.SelectedIndex == 1)
        {
            TextBox5.Text = "1000";

        }
        else if (DropDownList2.SelectedIndex == 2)
        {
            TextBox5.Text = "1500";

        }
        else if (DropDownList2.SelectedIndex == 3)
        {
            TextBox5.Text = "2000";

        }
        else
        {
            TextBox5.Text = "2500";

        }
    }
    protected void DropDownList3_SelectedIndexChanged(object sender, EventArgs e)
    {
        if (DropDownList3.SelectedIndex == 0)
        {
            TextBox6.Text = "1000";
        }
        else if (DropDownList3.SelectedIndex == 1)
        {
            TextBox6.Text = "750";
        }
        else if (DropDownList3.SelectedIndex == 2)
        {
            TextBox6.Text = "500";
        }
        else
        {
            TextBox6.Text = "0";
        }
    }
    protected void BtnSubmit_Click(object sender, EventArgs e)
    {
        st = "Insert into booking values('" + TextBox1.Text + "','" + TextBox2.Text + "','" + TextBox3.Text + "','" + DropDownList1.Text + "','" + DropDownList2.Text + "','" + DropDownList3.Text + "','" + TextBox6.Text + "','" + TextBox7.Text + "','" + TextBox8.Text + "')";
        cm = new OleDbCommand(st, db);
        cm.ExecuteNonQuery();
        Label1.Text = "Record Saved and Press Reset";
        Label1.ForeColor = System.Drawing.Color.Blue;
        BtnReset.Focus();
        BtnSubmit.Enabled = false;
    }
    protected void BtnConfirm_Click(object sender, EventArgs e)
    {
        double a;
        double b;
        double c;
        double d;
        double result1,result2;
        a = Convert.ToDouble(TextBox4.Text);
        b = Convert.ToDouble(TextBox5.Text);
        result1 = a + b;
        TextBox7.Text = Convert.ToString(result1);
        c = Convert.ToDouble(TextBox6.Text);
        d = Convert.ToDouble(TextBox7.Text);
        result2 = c + d;
        TextBox8.Text = Convert.ToString(result2);

    }
}
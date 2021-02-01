
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace LAB3D
{
    public partial class Form1 : Form
    {
        public Form1()
        {

            {
                InitializeComponent();
            }


        }
       
        private void textBox1_Enter(object sender, EventArgs e)
            {

            }

        private void textBox2_Enter(object sender, EventArgs e)
            {

            }

        private void textBox3_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox4_TextChanged(object sender, EventArgs e)
        {

        }


        private void button2_MouseClick(object sender, MouseEventArgs e)
        {
            while ((textBox2.Text == "*") || (textBox2.Text == "+") || (textBox2.Text == "/") || (textBox2.Text == "-"))
                
            {

                if (textBox2.Text == "/")
                {
                    textBox4.Text = textBoxDivide(textBox1.Text, textBox3.Text);
                    break;
                }
                else if (textBox2.Text == "*")
                {
                    textBox4.Text = textBoxMultiply(textBox1.Text, textBox3.Text);
                    break;
                }
                else if (textBox2.Text == "+")
                {

                    textBox4.Text = textBoxAdd(textBox1.Text, textBox3.Text);
                    break;
                }
                else if (textBox2.Text == "-")
                {
                    textBox4.Text = textBoxSubtract(textBox1.Text, textBox3.Text);
                    break;
                }
                else if ((textBox2.Text != "*") || (textBox2.Text != "+") || (textBox2.Text != "/") || (textBox2.Text != "-"))
                {
                    textBox4.Text = "Wrong operator, try again!";
                    break;
                   
                }

            }


        }

        public string textBoxAdd(string x, string y)
        {
            if (double.TryParse(x, out firstNum) && (double.TryParse(y, out secondNum)))
            {
                firstNum = double.Parse(x);
                secondNum = double.Parse(y);
            }
            else
            {
                string error = "Enter a correct nnumber";
                return error;
            }
            string theAnswer = Convert.ToString(firstNum + secondNum);
            return theAnswer;
        }

        public string textBoxSubtract(string x, string y)
        {
            if (double.TryParse(x, out firstNum) && (double.TryParse(y, out secondNum)))
            {
                firstNum = double.Parse(x);
                secondNum = double.Parse(y);
            }
            else
            {
                string error = "Enter a correct nnumber";
                return error;
            }
            string theAnswer = Convert.ToString(firstNum - secondNum);
            return theAnswer;
        }

        public string textBoxMultiply(string x, string y)
        {
            if (double.TryParse(x, out firstNum) && (double.TryParse(y, out secondNum)))
            {
                firstNum = double.Parse(x);
                secondNum = double.Parse(y);
            }
            else
            {
                string error = "Enter a correct nnumber";
                return error;
            }
            string theAnswer = Convert.ToString(firstNum * secondNum);
            return theAnswer;
        }

        double firstNum;
        double secondNum;
        public string textBoxDivide(string x, string y)
        {
            if (double.TryParse(x, out firstNum) && (double.TryParse(y, out secondNum)))
            {
                firstNum = double.Parse(x);
                secondNum = double.Parse(y);
            }
            else
            {
                string error = "Enter a correct nnumber";
                return error;
            }    
                string theAnswer = Convert.ToString(firstNum / secondNum);
                return theAnswer;
            
        }
    }
    
}

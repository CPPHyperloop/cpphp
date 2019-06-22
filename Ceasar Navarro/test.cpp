#include <Fl/Fl.H>
#include <FL/Fl_Window.H>
#include <FL/Fl_Button.H>
#include<FL/Fl_Output.H>
#include<Fl/Fl_Slider.H>
#include<string>
#include<unistd.h>
#include <ctime>
#include<cstdlib>
#include<iostream>
#include<time.h>
#include<stdio.h>


class GuiWindow : public Fl_Window
{
    //Fl_Window *window = new Fl_Window(340,180);
    // the input values that will be changing on the screen
    Fl_Output text;
    
    int r = rand() %10;
    

    /* 
    Fl_Input motorSpeed;
    Fl_Input motorCurrent;
    Fl_Input motorTempOne;
    Fl_Input motorTempTwo;
    */

    // The slider that indicates the start and finish 
    //Fl_Slider *startEndSlider;

    // The button that will have commands 
    /* 
    Fl_Button *brakesButton; 
    Fl_Button *powerButton;
    */


    inline void copyCbI()
    {
        const char *words [3];
        words[0] = "3";
        words[1] = "5";
        words[2] = "7";

        int counter = 0;
    
        text.value(words[counter]);
        text.redraw();

        counter++;

        if(counter ==3)
        {
            counter =0;
        }

       
        
    
        
     
    }

    static void copyCb(Fl_Widget* w, void *v)
    {
        ((GuiWindow*)v)->copyCbI();


    }

    const char* switchString(int num)
    {
        std::string s = std::to_string(num);
        const char* pchar = s.c_str();
        return pchar;

    }
    /* 
    inline void sliderCbI(Fl_Slider* slider) //CbI stands fot Callback incline 
    {
        text->value(slider->value());
    }

    static void sliderCb(Fl_Widget* W, void *v) // Cb stands for callback 
    {
        ((GuiWindow*)v)->sliderCbI((Slider*)w);
    }

    inline void powerButtonCbI()
    {


    }
    */ 


    public:
    GuiWindow(const char* label=0) : Fl_Window(340,180,label),text(50,20,100,20,"new")
    {
        text.value("10");
        Fl::check();
        usleep(100000);
        text.value("70");
        Fl::check();
        text.callback(copyCb,this); 
        
        text.redraw();

    }


    ~GuiWindow(){}


};




int main(int argc, char **argv)
{
    srand(time(0));
    GuiWindow CPP("CPPHyperloop");

    CPP.show(argc,argv);
    CPP.end();
    return Fl::run();

}



#include <Fl/Fl.H>
#include <FL/Fl_Window.H>
#include <FL/Fl_Button.H>
#include<FL/Fl_Input.H>
#include<Fl/Fl_Slider.H>
#include<string>
#include<unistd.h>
#include<iostream>

class GuiWindow : public Fl_Window
{
    private:

    // the input values that will be changing on the screen
    Fl_Input *text;

    /* 
    Fl_Input motorSpeed;
    Fl_Input motorCurrent;
    Fl_Input motorTempOne;
    Fl_Input motorTempTwo;
    */

    // The slider that indicates the start and finish 
    Fl_Slider *startEndSlider;

    // The button that will have commands 

    Fl_Button *brakesButton; 
    Fl_Button *powerButton;

    inline void copyCbI();

    static void copyCb(Fl_Widget* w, void *v);
   
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
    GuiWindow();
    GuiWindow(const char* label=0);


    ~GuiWindow(){}


};
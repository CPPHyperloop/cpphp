#include "GuiWindow.h"
#include <Fl/Fl.H>
#include <FL/Fl_Window.H>
#include <FL/Fl_Button.H>
#include<FL/Fl_Input.H>
#include<Fl/Fl_Slider.H>

GuiWindow:GuiWindow(const char* label=0):Fl_Window(340,180),text(10,10,100,20)
{
    text->callback(copyCb,this); 
}


inline void GuiWindow::copyCbI()
{
    const char *words [3];
    words[0] = "hi";
    words[1] = "bye";
    words[2] = "sup";

    for( int i = 0; i < 3; i++)
    {
        text->when(FL_WHEN_CHANGED);
        text->value(words[i]);
    }

}
 static void copyCb(Fl_Widget* w, void *v)
{
    ((GuiWindow*)v)->copyCbI();
}



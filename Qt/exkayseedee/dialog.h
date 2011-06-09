#ifndef DIALOG_H
#define DIALOG_H

#include <QDialog>
#include <string>

namespace Ui {
    class Dialog;
}

class Dialog : public QDialog
{
    Q_OBJECT

public:
    explicit Dialog(QWidget *parent = 0);
    ~Dialog();

private:
    Ui::Dialog *ui;
    void checkAnswer(int);
    QString getAlt(int);
    QString getTitle(int);

private slots:
    void ans1();
    void ans2();
    void ans3();
    void ans4();
    void ans5();
    void reload();
};

#endif // DIALOG_H

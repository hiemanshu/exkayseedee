/********************************************************************************
** Form generated from reading UI file 'dialog.ui'
**
** Created: 
**      by: Qt User Interface Compiler version 4.7.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_DIALOG_H
#define UI_DIALOG_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QDialog>
#include <QtGui/QGridLayout>
#include <QtGui/QHBoxLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QPushButton>
#include <QtGui/QTextBrowser>
#include <QtGui/QVBoxLayout>

QT_BEGIN_NAMESPACE

class Ui_Dialog
{
public:
    QHBoxLayout *horizontalLayout;
    QVBoxLayout *verticalLayout;
    QTextBrowser *altText;
    QLabel *scr;
    QGridLayout *gridLayout;
    QPushButton *ch1;
    QPushButton *ch2;
    QPushButton *ch3;
    QPushButton *ch4;
    QPushButton *ch5;
    QPushButton *rld;

    void setupUi(QDialog *Dialog)
    {
        if (Dialog->objectName().isEmpty())
            Dialog->setObjectName(QString::fromUtf8("Dialog"));
        Dialog->resize(800, 440);
        horizontalLayout = new QHBoxLayout(Dialog);
        horizontalLayout->setSpacing(6);
        horizontalLayout->setContentsMargins(11, 11, 11, 11);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        verticalLayout = new QVBoxLayout();
        verticalLayout->setSpacing(6);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        altText = new QTextBrowser(Dialog);
        altText->setObjectName(QString::fromUtf8("altText"));

        verticalLayout->addWidget(altText);

        scr = new QLabel(Dialog);
        scr->setObjectName(QString::fromUtf8("scr"));

        verticalLayout->addWidget(scr);


        horizontalLayout->addLayout(verticalLayout);

        gridLayout = new QGridLayout();
        gridLayout->setSpacing(6);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        ch1 = new QPushButton(Dialog);
        ch1->setObjectName(QString::fromUtf8("ch1"));
        ch1->setMinimumSize(QSize(150, 0));

        gridLayout->addWidget(ch1, 0, 0, 1, 1);

        ch2 = new QPushButton(Dialog);
        ch2->setObjectName(QString::fromUtf8("ch2"));
        ch2->setMinimumSize(QSize(150, 0));

        gridLayout->addWidget(ch2, 0, 1, 1, 1);

        ch3 = new QPushButton(Dialog);
        ch3->setObjectName(QString::fromUtf8("ch3"));
        ch3->setMinimumSize(QSize(150, 0));

        gridLayout->addWidget(ch3, 1, 0, 1, 1);

        ch4 = new QPushButton(Dialog);
        ch4->setObjectName(QString::fromUtf8("ch4"));
        ch4->setMinimumSize(QSize(150, 0));

        gridLayout->addWidget(ch4, 1, 1, 1, 1);

        ch5 = new QPushButton(Dialog);
        ch5->setObjectName(QString::fromUtf8("ch5"));
        ch5->setMinimumSize(QSize(150, 0));

        gridLayout->addWidget(ch5, 2, 0, 1, 1);

        rld = new QPushButton(Dialog);
        rld->setObjectName(QString::fromUtf8("rld"));
        rld->setMinimumSize(QSize(150, 0));

        gridLayout->addWidget(rld, 2, 1, 1, 1);


        horizontalLayout->addLayout(gridLayout);


        retranslateUi(Dialog);
        QObject::connect(ch1, SIGNAL(clicked()), Dialog, SLOT(ans1()));
        QObject::connect(ch2, SIGNAL(clicked()), Dialog, SLOT(ans2()));
        QObject::connect(ch3, SIGNAL(clicked()), Dialog, SLOT(ans3()));
        QObject::connect(ch4, SIGNAL(clicked()), Dialog, SLOT(ans4()));
        QObject::connect(ch5, SIGNAL(clicked()), Dialog, SLOT(ans5()));
        QObject::connect(rld, SIGNAL(clicked()), Dialog, SLOT(reload()));

        QMetaObject::connectSlotsByName(Dialog);
    } // setupUi

    void retranslateUi(QDialog *Dialog)
    {
        Dialog->setWindowTitle(QApplication::translate("Dialog", "Dialog", 0, QApplication::UnicodeUTF8));
        scr->setText(QApplication::translate("Dialog", "Score : 0", 0, QApplication::UnicodeUTF8));
        ch1->setText(QApplication::translate("Dialog", "PushButton", 0, QApplication::UnicodeUTF8));
        ch2->setText(QApplication::translate("Dialog", "PushButton", 0, QApplication::UnicodeUTF8));
        ch3->setText(QApplication::translate("Dialog", "PushButton", 0, QApplication::UnicodeUTF8));
        ch4->setText(QApplication::translate("Dialog", "PushButton", 0, QApplication::UnicodeUTF8));
        ch5->setText(QApplication::translate("Dialog", "PushButton", 0, QApplication::UnicodeUTF8));
        rld->setText(QApplication::translate("Dialog", "Reload", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class Dialog: public Ui_Dialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_DIALOG_H

#include "dialog.h"
#include "ui_dialog.h"
#include <QtSql/QSqlDatabase>
#include <QtSql/QSqlQuery>

int ans = 0;
int score = 0;

Dialog::Dialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::Dialog)
{
    ui->setupUi(this);
    QSqlDatabase db = QSqlDatabase::addDatabase("QSQLITE");
    db.setDatabaseName("data.db");
    db.open();
    Dialog::reload();

}

Dialog::~Dialog()
{
    delete ui;
}

void Dialog::ans1()
{
    Dialog::checkAnswer(1);
}

void Dialog::ans2()
{
    Dialog::checkAnswer(2);
}

void Dialog::ans3()
{
    Dialog::checkAnswer(3);
}

void Dialog::ans4()
{
    Dialog::checkAnswer(4);
}

void Dialog::ans5()
{
    Dialog::checkAnswer(5);
}

void Dialog::reload()
{
    int x = rand() % 900 + 1;
    QString altText = Dialog::getAlt(x);
    QString title = Dialog::getTitle(x);
    QString tit[5];
    for (int i=0; i<5; i++)
    {
        tit[i] = Dialog::getTitle(rand() % 900 + 1);
    }
    ans = rand() % 5;
    tit[ans] = title;
    ui->ch1->setText(tit[0]);
    ui->ch2->setText(tit[1]);
    ui->ch3->setText(tit[2]);
    ui->ch4->setText(tit[3]);
    ui->ch5->setText(tit[4]);
    ui->altText->setText(altText);
}

void Dialog::checkAnswer(int x)
{

    if (x == ans)
    {
        score += 1;
        QString scoreText = "Score : ";
        scoreText.append(QVariant(score).toString());
        Dialog::reload();
        ui->scr->setText(scoreText);
    }
    else
    {
        ui->altText->setText(QString("Wrong Answer, Try Again"));
    }
}

QString Dialog::getAlt(int id)
{
    QSqlQuery query;
    query.prepare("SELECT alt FROM COMICS WHERE ID = :id");
    query.bindValue(":id", id);
    query.exec();
    query.next();
    QString altText = query.value(0).toString();
    return altText;
}

QString Dialog::getTitle(int id)
{
    QSqlQuery query;
    query.prepare("SELECT title FROM COMICS WHERE ID = :id");
    query.bindValue(":id", id);
    query.exec();
    query.next();
    QString title = query.value(0).toString();
    return title;
}

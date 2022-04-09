<?php

namespace App\Controllers;

use \Core\View;

/**
 * Home Controller
 */
class Home extends \Core\Controller
{
    /**
     * Before Filter
     *
     * @return void
     */
    protected function before() 
    {
        // echo "(before) ";
        // return false;
    }

    /**
     * After Filter
     *
     * @return void
     */
    protected function after()
    {
        // echo " (after)";
    }
    
    /**
     * Show the index page
     * 
     * @return void
     */
    public function indexAction()
    {
        /*
        View::render('Home/index.php', [
            'name'      => 'Dave',
            'colors'   => ['red', 'green', 'blue'],
        ]);
        */
        View::renderTemplate('Home/index.html', [
            'name'      => 'Dave',
            'colours'   => ['red', 'green', 'blue']
        ]);
    }

}
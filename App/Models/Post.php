<?php

namespace App\Models;

use PDO;
use PDOException;

/**
 * Post model
 */
class Post extends \Core\Model
{
    /**
     * Get all the posts as an associative array
     * 
     * @return array
     */
    public static function getAll()
    {
        try {
            $db = static::getDB();

            $stmt = $db->query('SELECT id, title, content FROM posts
                                ORDER BY created_at');
            $result = $stmt->fetchAll(PDO::FETCH_ASSOC);

            return $result;

        } catch (PDOException $e) {
            echo $e->getMessage();
        }
    }
}
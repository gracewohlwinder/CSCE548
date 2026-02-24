[CmdletBinding()]
param()

begin {
    function Invoke-Request {
        [CmdletBinding()]
        param(
            [Parameter(Position = 0)]
            [String]
            $Endpoint,

            [Parameter(Position = 1)]
            [String]
            $Method = 'GET'
        )

        process {
            $Param = @{
                Uri             = "http://localhost:8000/${Endpoint}"
                Method          = $Method
                UseBasicParsing = $True
            }

            Write-Host "${Method}: $($Param.Uri)" -ForegroundColor 'Gray'

            Invoke-WebRequest @Param |
                Select-Object -ExpandProperty 'Content' |
                ConvertFrom-Json
        }
    }
}

process {
    Write-Host ''
    Write-Host (Invoke-Request 'users' | Out-String)

    $NewUsername = 'new_user1'
    Invoke-Request 'users?username=new_user1' 'POST'
    Write-Host (Invoke-Request 'users' | Out-String)


    $NewUser = Invoke-Request "users?username=${NewUsername}"
    Invoke-Request "users/$($NewUser.id)?username=updated_username" 'POST'
    Write-Host (Invoke-Request 'users' | Out-String)

    Invoke-Request "users/$($NewUser.id)" 'DELETE'
    Write-Host (Invoke-Request 'users' | Out-String)

    Write-Host (Invoke-Request 'users/1/followers' | Out-String)
    Invoke-Request 'users/1/followers?follower_id=4' 'POST'
    Write-Host (Invoke-Request 'users/1/followers' | Out-String)
    Invoke-Request 'users/1/followers?follower_id=4' 'DELETE'
    Write-Host (Invoke-Request 'users/1/followers' | Out-String)

    Write-Host (Invoke-Request 'users/1/posts' | Format-Table | Out-String)

    Invoke-Request 'users/1/posts?description=new post' 'POST'
    Write-Host (Invoke-Request 'users/1/posts' | Format-Table | Out-String)

    $NewPost = (Invoke-Request 'users/1/posts')[-1]
    Invoke-Request "posts/$($NewPost.id)?description=updated post" 'POST'
    Write-Host (Invoke-Request 'users/1/posts' | Format-Table | Out-String)

    Invoke-Request "posts/$($NewPost.id)" 'DELETE'
    Write-Host (Invoke-Request 'users/1/posts' | Format-Table | Out-String)

    Write-Host (Invoke-Request 'users/1/posts/deleted' | Format-Table | Out-String)

    $Post = (Invoke-Request 'users/1/posts')[0]
    Write-Host (Invoke-Request "posts/$($Post.id)/comments" | Format-Table | Out-String)
    Invoke-Request "posts/$($Post.id)/comments?comment=new comment&user_id=2" 'POST'
    Write-Host (Invoke-Request "posts/$($Post.id)/comments" | Format-Table | Out-String)

    $NewComment = (Invoke-Request "posts/$($Post.id)/comments")[-1]
    Invoke-Request "comments/$($NewComment.id)?comment=updated comment" 'POST'
    Write-Host (Invoke-Request "posts/$($Post.id)/comments" | Format-Table | Out-String)

    Invoke-Request "comments/$($NewComment.id)" 'DELETE'
    Write-Host (Invoke-Request "posts/$($Post.id)/comments" | Format-Table | Out-String)

    Write-Host (Invoke-Request "posts/$($Post.id)/comments/deleted" | Format-Table | Out-String)

    $Post = (Invoke-Request 'users/1/posts')[0]
    Write-Host (Invoke-Request "posts/$($Post.id)/favorites" | Format-Table | Out-String)
    Invoke-Request "posts/$($Post.id)/favorites?user_id=5" 'POST'
    Write-Host (Invoke-Request "posts/$($Post.id)/favorites" | Format-Table | Out-String)

    Invoke-Request "posts/$($Post.id)/favorites?user_id=5" 'DELETE'
    Write-Host (Invoke-Request "posts/$($Post.id)/favorites" | Format-Table | Out-String)
}
